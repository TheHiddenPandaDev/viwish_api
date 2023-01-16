from dataclasses import dataclass

@dataclass
class CreateLogCommand:
    action_type: str
    id_user: int
    id_user_referred: int
    description: str
