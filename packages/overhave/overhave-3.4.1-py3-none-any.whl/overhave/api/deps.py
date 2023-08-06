from functools import cache
from pathlib import Path

from overhave.api.settings import OverhaveApiAuthSettings
from overhave.entities import OverhaveRedisSettings
from overhave.storage import (
    DraftStorage,
    FeatureStorage,
    FeatureTagStorage,
    IDraftStorage,
    IFeatureStorage,
    IFeatureTagStorage,
    ISystemUserStorage,
    ITestUserStorage,
    SystemUserStorage,
    TestRunStorage,
    TestUserStorage,
)
from overhave.transport import EmulationTask, PublicationTask, RedisProducer, RedisStream, TestRunTask


@cache
def get_api_auth_settings() -> OverhaveApiAuthSettings:
    return OverhaveApiAuthSettings()


@cache
def get_admin_files_dir() -> Path:
    return Path(__file__).parent.parent / "admin" / "files"


@cache
def get_system_user_storage() -> ISystemUserStorage:
    return SystemUserStorage()


@cache
def get_feature_tag_storage() -> IFeatureTagStorage:
    return FeatureTagStorage()


@cache
def get_feature_storage() -> IFeatureStorage:
    return FeatureStorage()


@cache
def get_draft_storage() -> IDraftStorage:
    return DraftStorage()


@cache
def get_test_user_storage() -> ITestUserStorage:
    return TestUserStorage()


@cache
def get_test_run_storage() -> TestRunStorage:
    return TestRunStorage()


@cache
def get_redis_producer() -> RedisProducer:
    return RedisProducer(
        settings=OverhaveRedisSettings(),
        mapping={
            TestRunTask: RedisStream.TEST,
            PublicationTask: RedisStream.PUBLICATION,
            EmulationTask: RedisStream.EMULATION,
        },
    )
