from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Extra
from pydantic import parse_obj_as


class Limit(BaseModel):
    max_image_count: Optional[int]
    remaining_image_count: int


class UserLimits(BaseModel):
    user_limit: Optional[Limit]
    project_limit: Limit
    folder_limit: Limit


class UploadAnnotationAuthData(BaseModel):
    access_key: str
    secret_key: str
    session_token: str
    region: str
    bucket: str
    images: Dict[int, dict]

    class Config:
        extra = Extra.allow
        fields = {
            "access_key": "accessKeyId",
            "secret_key": "secretAccessKey",
            "session_token": "sessionToken",
            "region": "region",
        }

    def __init__(self, **data):
        credentials = data["creds"]
        data.update(credentials)
        del data["creds"]
        super().__init__(**data)


class DownloadMLModelAuthData(BaseModel):
    access_key: str
    secret_key: str
    session_token: str
    region: str
    bucket: str
    paths: List[str]

    class Config:
        extra = Extra.allow
        fields = {
            "access_key": "accessKeyId",
            "secret_key": "secretAccessKey",
            "session_token": "sessionToken",
            "region": "region",
        }

    def __init__(self, **data):
        credentials = data["tokens"]
        data.update(credentials)
        del data["tokens"]
        super().__init__(**data)


class UploadCustomFieldValues(BaseModel):
    succeeded_items: Optional[List[Any]]
    failed_items: Optional[List[str]]
    error: Optional[Any]


class ServiceResponse(BaseModel):
    status: int
    reason: str
    content: Union[bytes, str]
    data: Any

    def __init__(self, response, content_type=None):
        data = {
            "status": response.status_code,
            "reason": response.reason,
            "content": response.content,
        }
        try:
            if content_type and content_type is not self.__class__:
                data["data"] = parse_obj_as(content_type, response.json())
            else:
                data["data"] = response.json()
        except Exception as e:
            data["data"] = {}
        super().__init__(**data)

    @property
    def ok(self):
        return 199 < self.status < 300

    @property
    def error(self):
        default_message = self.reason if self.reason else "Unknown Error"
        if isinstance(self.data, dict):
            return self.data.get("error", default_message)
        else:
            return getattr(self.data, "error", default_message)
