from dataclasses import dataclass


@dataclass
class Contest:
    id: int
    name: str
    # CF, IOI, ICPC
    type: str
    # BEFORE, CODING, PENDING_SYSTEM_TEST, SYSTEM_TEST, FINISHED
    phase: str
    frozen: bool
    duration_seconds: int
    start_time_seconds: int
    relative_time_seconds: int
    prepared_by: str
    website_url: str
    description: str
    difficulty: int
    #  Official ICPC Contest, Official School Contest, Opencup Contest,
    #  School/University/City/Region Championship, Training Camp Contest,
    #  Official International Personal Contest, Training Contest.
    kind: str
    icpc_region: str
    country: str
    city: str
    season: str
