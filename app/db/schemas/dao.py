from pydantic import BaseModel
import typing as t


class DaoBasic(BaseModel):
    id: int
    dao_name: t.Optional[str]
    dao_short_description: t.Optional[str]
    dao_url: str
    governance_id: t.Optional[int]
    tokenomics_id: t.Optional[int]
    design_id: t.Optional[int]
    is_draft: t.Optional[bool]
    is_published: t.Optional[bool]
    nav_stage: t.Optional[int]
    is_review: t.Optional[bool]

    class Config:
        orm_mode = True


class CreateOrUpdateFooterSocialLinks(BaseModel):
    social_network: t.Optional[str]
    link_url: t.Optional[str]


class FooterSocialLinks(CreateOrUpdateFooterSocialLinks):
    id: int

    class Config:
        orm_mode = True


class CreateOrUpdateDaoDesign(BaseModel):
    theme_id: int
    logo_url: t.Optional[str]
    show_banner: t.Optional[bool]
    banner_url: t.Optional[str]
    show_footer: t.Optional[bool]
    footer_text: t.Optional[str]
    footer_social_links: t.List[CreateOrUpdateFooterSocialLinks]


class DaoDesign(CreateOrUpdateDaoDesign):
    id: int
    footer_social_links: t.List[FooterSocialLinks]

    class Config:
        orm_mode = True


class CreateOrUpdateGovernance(BaseModel):
    is_optimistic: t.Optional[bool]
    is_quadratic_voting: t.Optional[bool]
    time_to_challenge__sec: t.Optional[int]
    quorum: t.Optional[int]
    vote_duration__sec: t.Optional[int]
    amount: t.Optional[float]
    currency: t.Optional[str]
    support_needed: t.Optional[int]
    governance_whitelist: t.List[int]  # user_id


class Governance(CreateOrUpdateGovernance):
    id: int

    class Config:
        orm_mode = True


class CreateOrUpdateTokenHolder(BaseModel):
    user_id: int
    percentage: t.Optional[float]
    balance: t.Optional[float]


class TokenHolder(CreateOrUpdateTokenHolder):
    id: int

    class Config:
        orm_mode = True


class CreateOrUpdateDistribution(BaseModel):
    distribution_type: str
    balance: t.Optional[float]
    percentage: t.Optional[float]
    # distributions have a highly flexible pattern
    additionalDetails: dict


class Distribution(CreateOrUpdateDistribution):
    id: int

    class Config:
        orm_mode = True


class CreateOrUpdateTokenomics(BaseModel):
    type: str
    token_name: t.Optional[str]
    token_ticker: t.Optional[str]
    token_amount: t.Optional[float]
    token_image_url: t.Optional[str]
    token_remaining: t.Optional[float]
    is_activated: t.Optional[bool]
    token_holders: t.List[CreateOrUpdateTokenHolder]
    distributions: t.List[CreateOrUpdateDistribution]


class Tokenomics(CreateOrUpdateTokenomics):
    id: int
    token_holders: t.List[TokenHolder]
    distributions: t.List[Distribution]


class CreateOrUpdateDao(BaseModel):
    dao_name: str
    dao_short_description: t.Optional[str]
    dao_url: str
    governance: CreateOrUpdateGovernance
    tokenomics: CreateOrUpdateTokenomics
    design: CreateOrUpdateDaoDesign
    is_draft: t.Optional[bool]
    is_published: t.Optional[bool]
    nav_stage: t.Optional[int]
    is_review: t.Optional[bool]


class Dao(CreateOrUpdateDao):
    id: int
    governance: t.Optional[Governance]
    tokenomics: t.Optional[Tokenomics]
    design: t.Optional[DaoDesign]

    class Config:
        orm_mode = True
