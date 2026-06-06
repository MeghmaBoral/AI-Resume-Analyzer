from pydantic import BaseModel
from typing import List


class Project(BaseModel):
    title: str
    description: str
    tech_stack: List[str]


class CandidateProfile(BaseModel):
    name: str
    email: str
    phone: str

    skills: List[str]

    education: List[str]

    experience: List[str]

    projects: List[Project]