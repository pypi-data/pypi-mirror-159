import logging

from pydantic import BaseModel, Field
from typing import List, Any

from ..json import Config
from ..utils import create_ui_path

LOGGER = logging.getLogger(__name__)
class ProfilePicture(BaseModel):
    """
        API Response data
    """
    id: int = Field(0, alias="avatarId")

    """
        Custom add data
    """
    url: str = ""

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

        # Get character
        LOGGER.debug(f"=== Avatar ===")
        LOGGER.debug(f"Getting character wtih id: {data['avatarId']}")
        character = Config.DATA["characters"].get(str(data["avatarId"]))
        if not character:
            LOGGER.error(f"Character not found with id: {data['avatarId']}")
            return
            
        __pydantic_self__.url = create_ui_path(character["sideIconName"].replace("_Side", ""))

class showAvatar(BaseModel):
    """
        API Response data
    """
    id: str = Field(0, alias="avatarId")
    level: int = 1

    """
        Custom data
    """
    name: str = ""
    icon:  str = ""

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

        # Get character
        LOGGER.debug(f"=== Character preview ===")
        LOGGER.debug(f"Getting character preview wtih id: {__pydantic_self__.id}")
        character_preview = Config.DATA["characters"].get(str(data["avatarId"]))

        if not character_preview:
            LOGGER.error(f"Character preview not found with id: {__pydantic_self__.id}")
            return

        __pydantic_self__.icon = create_ui_path(character_preview["sideIconName"].replace("_Side", ""))

        # Get name hash map
        LOGGER.debug(f"Getting name hash map id: {character_preview['nameTextMapHash']}")
        _name = Config.HASH_MAP["characters"].get(str(character_preview["nameTextMapHash"]))

        if _name is None:
            LOGGER.error(f"Name hash map not found.")
            return 

        __pydantic_self__.name = _name[Config.LANGS]
        

class Namecard(BaseModel):
    id: int = 0
    icon: str = ""
    banner: str = ""
    navbar: str = ""
    name: str = ""

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

        if __pydantic_self__.id > 0:
            LOGGER.debug(f"=== Namecard ===")
            LOGGER.debug(f"Getting namecard wtih id: {__pydantic_self__.id}")
            # Get name card
            namecard = Config.DATA["namecards"].get(str(__pydantic_self__.id))

            if not namecard:
                LOGGER.error(f"Namecard not found with id: {__pydantic_self__.id}")
                return

            __pydantic_self__.icon = create_ui_path(namecard["icon"])
            __pydantic_self__.banner = create_ui_path(namecard["picPath"][1])
            __pydantic_self__.navbar = create_ui_path(namecard["picPath"][0])

            LOGGER.debug(f"Getting name hash map id: {namecard['nameTextMapHash']}")
            _name = Config.HASH_MAP["namecards"].get(str(namecard["nameTextMapHash"]))
            if _name is None:
                LOGGER.error(f"Name hash map not found.")
                return 

            __pydantic_self__.name = _name[Config.LANGS]

class PlayerInfo(BaseModel):
    """
        API Response data
    """
    # Profile info
    achievement: int = Field(0, alias="finishAchievementNum")
    level: int = 0
    nickname: str = ""
    signature: str = ""
    world_level: int = Field(1, alias="worldLevel")
    icon: ProfilePicture = Field(None, alias="profilePicture")
    # Avatars
    characters_preview: List[showAvatar] = Field([], alias="showAvatarInfoList")
    # Abyss floor
    abyss_floor: int = Field(0, alias="towerFloorIndex")
    abyss_room: int = Field(0, alias="towerLevelIndex")

    """
        Custom data
    """
    namecard: Namecard = Namecard() # Profile namecard
    list_namecard: List[Namecard] = [] # List namecard preview in profile

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
        __pydantic_self__.namecard = Namecard(id=data["nameCardId"])
        __pydantic_self__.list_namecard = [Namecard(id=namecard) for namecard in data["showNameCardIdList"]]