import os
from injector import Module, provider, singleton

class EnvModule(Module):
    @provider
    @singleton
    def provide_stage(self) -> str:
        # TODO: generalize with .bind()? or a file with a bunch of typing.NewType()
        # https://github.com/python-injector/injector/issues/174#issuecomment-754702397
        # https://github.com/python-injector/injector/issues/133#issuecomment-577123634
        return os.getenv("STAGE")
