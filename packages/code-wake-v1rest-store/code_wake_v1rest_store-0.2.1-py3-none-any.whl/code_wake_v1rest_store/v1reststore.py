"""V1 REST API client store module."""


from __future__ import annotations

import json
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Optional, Tuple

import requests
from code_wake.config import Config
from code_wake.stack_trace import Stacktrace


class V1RestStore:
    """V1 REST API client store."""

    class Base:
        pass

    class Environment(Base):
        def __init__(self, store, id=None, name=None):
            self._store = store
            self.id = id
            self.name = name

        def __repr__(self):
            return f"<V1RestStore.Environment(id='{self.id}')>"

    class Process(Base):
        def __init__(
            self,
            store,
            id=None,
            run_ts=None,
            environment_id=None,
            pid=None,
            username=None,
            fqdn=None,
            exe_path=None,
            app_id=None,
            app_vsn_id=None,
        ):
            self._store = store
            self.id = id
            self.run_ts = run_ts
            self.environment_id = environment_id
            self.pid = pid
            self.username = username
            self.fqdn = fqdn
            self.exe_path = exe_path
            self.app_id = app_id
            self.app_vsn_id = app_vsn_id

        @property
        def environment(self):
            if hasattr(self, "_environment"):
                return self._environment

            if self.environment_id is None:
                self._environment = None
            else:
                with self._store.session() as session:
                    res = session.get(f"{self._store._base_url}/environments/{self.environment_id}")
                    if res.status_code == 404:
                        self._environment = None
                    else:
                        if res.status_code != 200:
                            self._store.req_res_raise(res, 'getting process with ID "{id}"')

                        json_data = res.json()

                        self._environment = V1RestStore.Environment(
                            store=self._store,
                            id=json_data["id"],
                            name=json_data["name"],
                        )

            return self._environment

        @property
        def app(self):
            if hasattr(self, "_app"):
                return self._app

            if self.app_id is None:
                self._app = None
            else:
                with self._store.session() as session:
                    res = session.get(f"{self._store._base_url}/apps/{self.app_id}")
                    if res.status_code == 404:
                        self._app = None
                    else:
                        if res.status_code != 200:
                            self._store.req_res_raise(res, 'error getting process with ID "{id}"')

                        json_data = res.json()

                        self._app = V1RestStore.App(
                            store=self._store,
                            id=json_data["id"],
                            name=json_data["name"],
                        )

            return self._app

        def __repr__(self):
            return f"<V1RestStore.Process(id='{self.id}')>"

        @property
        def app_vsn(self):
            if hasattr(self, "_app_vsn"):
                return self._app_vsn

            if self.app_vsn_id is None:
                self._app_vsn = None
            else:
                with self._store.session() as session:
                    res = session.get(f"{self._store._base_url}/app_vsns/{self.app_vsn_id}")
                    if res.status_code == 404:
                        self._app_vsn = None
                    else:
                        if res.status_code != 200:
                            self.req_res_raise(res, 'error getting process with ID "{id}"')

                        json_data = res.json()

                        self._app_vsn = V1RestStore.AppVsn(
                            store=self._store,
                            id=json_data["id"],
                            vsn=json_data["vsn"],
                        )

            return self._app_vsn

    class App(Base):
        def __init__(self, store, id=None, name=None):
            self.id = id
            self._store = store
            self.name = name

        def __repr__(self):
            return f"<V1RestStore.App(id='{self.id}')>"

    class AppVsn(Base):
        def __init__(self, store, id=None, vsn=None):
            self._store = store
            self.id = id
            self.vsn = vsn

        def __repr__(self):
            return f"<V1RestStore.AppVsn(id='{self.id}')>"

    class Event(Base):
        def __init__(self, store, id, when_ts, process_id, digest, stacktrace_id, stacktrace, data):
            self._store = store
            self.id = id
            self.when_ts = when_ts or datetime.now().timestamp()
            self.process_id = process_id
            self.digest = digest
            self.stacktrace = stacktrace
            self.stacktrace_id = stacktrace_id
            self.data = data

        def __repr__(self):
            return f"<V1RestStore.Event(id='{self.id}')>"

    class EventData(Base):
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val

        def __repr__(self):
            return f"<V1RestStore.EventData(id='{self.id}')>"

    class Stacktrace(Base):
        def __init__(self, id, digest, stackframes):
            self.id = id
            self.digest = digest
            self.stackframes = stackframes

        def __repr__(self):
            return f"<V1RestStore.Stacktrace(id='{self.id}')>"

    class Stackframe(Base):
        def __init__(self, stacktrace_id=None, filename=None, lineno=None, src=None):
            self.id = id
            self.stacktrace_id = stacktrace_id
            self.filename = filename
            self.lineno = lineno
            self.src = src

        def __repr__(self):
            return f"<V1RestStore.Stacktrace(id='{self.id}')>"

    def __init__(self, base_url: str, *args, username: str = None, password: str = None, **kwargs):
        self._base_url = base_url
        self._username = username
        self._password = password

    def session(self):
        s = requests.Session()
        if self._username and self._password:
            s.auth = (self._username, self._password)

        return s

    def insert_app(self, name: str, vsn: Optional[str] = None) -> V1RestStore.App:
        with self.session() as session:
            res = session.post(
                f"{self._base_url}/apps", json={"name": name, "vsn": vsn}, headers={"content-type": "application/json"}
            )
            if res.status_code != 201:
                self.req_res_raise(res, 'creating app with name "{name}"')

            json_data = res.json()

            return V1RestStore.App(store=self, id=json_data["id"], name=json_data["name"])

    def get_environment_by_id(self, id: int) -> Optional[V1RestStore.Environment]:
        with self.session() as session:
            res = session.get(f"{self._base_url}/environments/{id}")
            if res.status_code == 404:
                return None
            if res.status_code != 200:
                self.req_res_raise(res, f'getting environment with ID "{id}"')

            json_data = res.json()

            return V1RestStore.Environment(
                store=self,
                id=json_data["id"],
                name=json_data["name"],
            )

    def get_app_by_id(self, id: int) -> Optional[V1RestStore.App]:
        with self.session() as session:
            res = session.get(f"{self._base_url}/apps/{id}")
            if res.status_code == 404:
                return None
            if res.status_code != 200:
                self.req_res_raise(res, f'getting app with ID "{id}"')

            json_data = res.json()

            return V1RestStore.Environment(
                store=self,
                id=json_data["id"],
                name=json_data["name"],
            )

    def get_app_vsn_by_id(self, id: int) -> Optional[V1RestStore.AppVsn]:
        with self.session() as session:
            res = session.get(f"{self._base_url}/app_vsns/{id}")
            if res.status_code == 404:
                return None
            if res.status_code != 200:
                self.req_res_raise(res, f'getting app version with ID "{id}"')

            json_data = res.json()

            return V1RestStore.Environment(
                store=self,
                id=json_data["id"],
                vsn=json_data["vsn"],
            )

    def get_process_by_id(self, id: int) -> Optional[V1RestStore.Process]:
        with self.session() as session:
            res = session.get(f"{self._base_url}/processes/{id}")
            if res.status_code == 404:
                return None
            if res.status_code != 200:
                self.req_res_raise(res, f'getting process with ID "{id}"')

            json_data = res.json()

            return V1RestStore.Process(
                store=self,
                id=json_data["id"],
                environment_id=json_data["environment_id"],
                app_id=json_data["app_id"],
                app_vsn_id=json_data["app_vsn_id"],
                run_ts=json_data["run_ts"],
                pid=json_data["pid"],
                username=json_data["username"],
                fqdn=json_data["fqdn"],
                exe_path=json_data["exe_path"],
            )

    def insert_process(self, unstored_process: Process) -> V1RestStore.Process:
        with self.session() as session:
            res = session.post(
                f"{self._base_url}/processes",
                json={
                    "environment": None if unstored_process.environment is None else unstored_process.environment.name,
                    "app": unstored_process.app.name,
                    "app_vsn": None if unstored_process.app_vsn is None else unstored_process.app_vsn.vsn,
                    "pid": unstored_process.pid,
                    "username": unstored_process.username,
                    "fqdn": unstored_process.fqdn,
                    "exe_path": unstored_process.exe_path,
                },
                headers={"content-type": "application/json"},
            )
            if res.status_code != 201:
                self.req_res_raise(res, "creating process")

            json_data = res.json()

            return self.Process(
                store=self,
                id=json_data["id"],
                environment_id=json_data["environment_id"],
                run_ts=json_data["run_ts"],
                app_id=json_data["app_id"],
                app_vsn_id=json_data["app_vsn_id"],
                pid=json_data["pid"],
                username=json_data["username"],
                fqdn=json_data["fqdn"],
                exe_path=json_data["exe_path"],
            )

    def req_res_raise(self, res, msg):
        msg = None

        try:
            json_data = res.json()
            if "error" in json_data:
                msg = json_data["error"]
            else:
                msg = f"error {msg}, HTTP status {res.status_code} body {repr(res.data.decode())}"
        except Exception:
            msg = "unknown"

        raise Exception(f"error {msg}, HTTP status {res.status_code}")

    def insert_event(
        self,
        op_process: Process,
        data: Optional[Iterable[Tuple[str, str]]] = None,
        exc: Exception = None,
        inc_st: bool = None,
        st_len: Optional[int] = None,
        st_data: Optional[List[str, int, str]] = None,
        when_ts: float = None,
        sync: bool = False,
    ) -> Optional[V1RestStore.Event]:
        with self.session() as session:
            if inc_st is None:
                inc_st = Config()["stacktraces"]["include"]["for_non_exceptions" if exc is None else "from_exceptions"]

            if inc_st:
                if st_data is not None:
                    st = Stacktrace.from_data(st_data, st_len=st_len)
                elif exc is not None:
                    st = Stacktrace.from_exc(exc, st_len=st_len)
                else:
                    st = Stacktrace.from_caller(st_len=st_len)

            res = session.post(
                f"{self._base_url}/events",
                params={"sync": "true" if sync else "false"},
                json={
                    "process_id": op_process.id,
                    "stacktrace": st.data() if inc_st else None,
                    "data": data,
                    "when_ts": when_ts,
                },
                headers={"content-type": "application/json"},
            )

            event_record = None

            if sync:
                if res.status_code != 201:
                    self.req_res_raise(res, "creating event")

                json_data = res.json()

                stacktrace = None
                if inc_st:
                    stacktrace = V1RestStore.Stacktrace(
                        id=json_data["stacktrace"]["id"],
                        digest=json_data["stacktrace"]["digest"],
                        stackframes=[
                            V1RestStore.Stackframe(
                                stacktrace_id=json_data["stacktrace"]["id"],
                                filename=sf[0],
                                lineno=sf[1],
                                src=sf[2],
                            )
                            for sf in reversed(st.data())
                        ],
                    )

                event_record = V1RestStore.Event(
                    store=self,
                    id=json_data["id"],
                    when_ts=json_data["when_ts"],
                    process_id=op_process.id,
                    digest=json_data["digest"],
                    stacktrace_id=None if json_data["stacktrace"] is None else json_data["stacktrace"]["id"],
                    stacktrace=stacktrace,
                    data=None if data is None else [V1RestStore.EventData(key=key, val=val) for key, val in data],
                )
            else:
                if res.status_code != 202:
                    self.req_res_raise(res, "creating event")

            return event_record

    def get_events_by_data(
        self, where: Iterable[Tuple[str, str]], process_id: Optional[str] = None
    ) -> List[V1RestStore.Event]:
        with self.session() as session:
            qs_params = {"where": ",".join(f"{k}={v}" for k, v in where)}

            if process_id is not None:
                qs_params["process_id"] = process_id

            res = session.get(f"{self._base_url}/events", params=qs_params)

            json_data = res.json()

            return [
                V1RestStore.Event(
                    store=self,
                    id=ed["id"],
                    when_ts=ed["when_ts"],
                    process_id=ed["process_id"],
                    digest=ed["digest"],
                    stacktrace_id=None if ed["stacktrace"] is None else ed["stacktrace"]["id"],
                    stacktrace=None
                    if ed["stacktrace"] is None
                    else V1RestStore.Stacktrace(
                        id=ed["stacktrace"]["id"],
                        digest=ed["stacktrace"]["digest"],
                        stackframes=[
                            V1RestStore.Stackframe(
                                stacktrace_id=ed["stacktrace"]["id"],
                                filename=sf[0],
                                lineno=sf[1],
                                src=sf[2],
                            )
                            for sf in ed["stacktrace"]["stackframes"]
                        ],
                    ),
                    data=None
                    if ed["data"] is None
                    else [V1RestStore.EventData(key=key, val=val) for key, val in ed["data"]],
                )
                for ed in res.json()
            ]

    def get_processes(
        self,
        app_id: Optional[int] = None,
        from_ts: Optional[float] = None,
        to_ts: Optional[float] = None,
    ) -> List[V1RestStore.Event]:
        with self.session() as session:
            qs_params = {}
            if app_id is not None:
                qs_params["app_id"] = app_id
            if from_ts is not None:
                qs_params["from_ts"] = from_ts
            if to_ts is not None:
                qs_params["to_ts"] = to_ts

            res = session.get(f"{self._base_url}/processes", params=qs_params)

            json_data = res.json()

            return [
                V1RestStore.Process(
                    store=self,
                    id=pd["id"],
                    environment_id=pd["environment_id"],
                    run_ts=pd["run_ts"],
                    app_id=pd["app_id"],
                    app_vsn_id=pd["app_vsn_id"],
                    pid=pd["pid"],
                    username=pd["username"],
                    fqdn=pd["fqdn"],
                    exe_path=pd["exe_path"],
                )
                for pd in res.json()
            ]
