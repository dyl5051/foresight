"""Mock data for Foresight.

Replace this module with LLM-generated analysis by implementing a provider
that returns list[Event].  The rest of the app imports `get_events()` and
`get_event_by_id()` — swap the implementation without touching the API layer.
"""

from .models import Event, Scenario

EVENTS: list[Event] = [
    Event(
        id="us-china-tariffs-2026",
        title="US–China Tariff Escalation",
        category="economy",
        summary=(
            "The United States has announced a new round of tariffs targeting "
            "Chinese semiconductors and EV batteries, prompting Beijing to "
            "signal retaliatory measures on American agricultural exports."
        ),
        actors=["US Trade Representative", "China's Ministry of Commerce", "WTO"],
        scenarios=[
            Scenario(
                title="Negotiated De-escalation",
                description=(
                    "Both sides agree to a 90-day cooling-off period and resume "
                    "bilateral trade talks, resulting in partial tariff rollbacks."
                ),
                probability=0.30,
                implications=(
                    "Markets rally on reduced uncertainty; semiconductor supply "
                    "chains stabilize; agricultural futures ease."
                ),
            ),
            Scenario(
                title="Tit-for-Tat Escalation",
                description=(
                    "China retaliates with matching tariffs on US agriculture "
                    "and rare-earth export controls. The US responds with further "
                    "restrictions on AI chip exports."
                ),
                probability=0.40,
                implications=(
                    "Global equity markets sell off; inflation expectations rise; "
                    "allied nations pressured to pick sides on tech standards."
                ),
            ),
            Scenario(
                title="Third-Party Mediation",
                description=(
                    "The EU and ASEAN bloc propose a multilateral framework to "
                    "mediate, leading to a temporary standstill agreement."
                ),
                probability=0.15,
                implications=(
                    "Strengthens multilateral trade institutions; mild positive "
                    "for emerging-market currencies pegged to trade stability."
                ),
            ),
            Scenario(
                title="Decoupling Acceleration",
                description=(
                    "Talks collapse entirely. Both economies accelerate "
                    "onshoring and friend-shoring strategies."
                ),
                probability=0.15,
                implications=(
                    "Long-term reshaping of global supply chains; higher "
                    "consumer prices in the short term; strategic industries "
                    "see massive government investment."
                ),
            ),
        ],
        date="2026-04-10",
        region="Global",
    ),
    Event(
        id="eu-ai-act-enforcement",
        title="EU AI Act Enforcement Begins",
        category="tech",
        summary=(
            "The European Union has started enforcing the AI Act's high-risk "
            "provisions, requiring compliance audits for foundation-model "
            "providers operating in the single market."
        ),
        actors=[
            "European Commission",
            "OpenAI",
            "Google DeepMind",
            "Anthropic",
            "Meta AI",
        ],
        scenarios=[
            Scenario(
                title="Smooth Compliance",
                description=(
                    "Major providers meet requirements ahead of schedule, "
                    "establishing the EU as the global regulatory benchmark."
                ),
                probability=0.25,
                implications=(
                    "Brussels Effect accelerates AI governance worldwide; "
                    "compliance costs become a barrier to smaller entrants."
                ),
            ),
            Scenario(
                title="Partial Market Exit",
                description=(
                    "One or more US-based providers restrict EU access to "
                    "certain models, citing disproportionate compliance burden."
                ),
                probability=0.30,
                implications=(
                    "EU consumers lose access to cutting-edge models; European "
                    "AI startups gain market share; transatlantic tech tensions rise."
                ),
            ),
            Scenario(
                title="Legal Challenge",
                description=(
                    "A coalition of tech companies files suit at the European "
                    "Court of Justice, arguing the Act exceeds EU competences."
                ),
                probability=0.20,
                implications=(
                    "Regulatory uncertainty persists for 12–18 months; "
                    "investment in EU AI ventures slows."
                ),
            ),
            Scenario(
                title="Regulatory Fragmentation",
                description=(
                    "Individual member states interpret the Act differently, "
                    "creating a patchwork of enforcement regimes."
                ),
                probability=0.25,
                implications=(
                    "Increased compliance complexity; forum-shopping by AI "
                    "companies; pressure on the Commission to centralize enforcement."
                ),
            ),
        ],
        date="2026-04-12",
        region="Europe",
    ),
    Event(
        id="india-general-election-2026",
        title="India Snap Election Called",
        category="politics",
        summary=(
            "India's president has dissolved the Lok Sabha and called snap "
            "elections after a coalition realignment. The BJP-led NDA faces "
            "a reinvigorated INDIA opposition bloc."
        ),
        actors=["BJP / NDA", "INDIA Bloc", "Election Commission of India"],
        scenarios=[
            Scenario(
                title="NDA Retains Majority",
                description=(
                    "The BJP-led alliance wins a comfortable majority, "
                    "continuing current economic and foreign-policy trajectories."
                ),
                probability=0.35,
                implications=(
                    "Policy continuity reassures foreign investors; India's "
                    "manufacturing push and defense modernization stay on track."
                ),
            ),
            Scenario(
                title="INDIA Bloc Wins",
                description=(
                    "The opposition coalition secures a slim majority, "
                    "promising expanded social spending and labor reforms."
                ),
                probability=0.25,
                implications=(
                    "Rupee volatility in the short term; potential renegotiation "
                    "of free-trade agreements; boost to rural consumption."
                ),
            ),
            Scenario(
                title="Hung Parliament",
                description=(
                    "Neither bloc wins a majority, leading to protracted "
                    "coalition negotiations."
                ),
                probability=0.25,
                implications=(
                    "Policy paralysis risk; credit-rating agencies place India "
                    "on watch; FDI decisions delayed."
                ),
            ),
            Scenario(
                title="BJP Supermajority",
                description=(
                    "A wave election gives BJP a two-thirds supermajority, "
                    "enabling constitutional amendments."
                ),
                probability=0.15,
                implications=(
                    "Markets initially positive on strong mandate; civil-society "
                    "concerns over checks and balances; geopolitical weight of "
                    "India increases."
                ),
            ),
        ],
        date="2026-04-08",
        region="South Asia",
    ),
    Event(
        id="opec-production-cut-2026",
        title="OPEC+ Emergency Production Cut",
        category="economy",
        summary=(
            "OPEC+ has announced an emergency 2-million-barrel-per-day "
            "production cut in response to falling crude prices, raising "
            "concerns about energy costs heading into summer."
        ),
        actors=["Saudi Arabia", "Russia", "UAE", "US shale producers"],
        scenarios=[
            Scenario(
                title="Price Stabilization",
                description=(
                    "Crude settles in the $85–$95 range. Consumer impact is "
                    "moderate and inflation expectations remain anchored."
                ),
                probability=0.35,
                implications=(
                    "Central banks hold rates steady; energy equities outperform; "
                    "renewable-energy investment case strengthens at the margin."
                ),
            ),
            Scenario(
                title="Price Spike Above $110",
                description=(
                    "Cuts coincide with summer demand surge and a Gulf "
                    "shipping disruption, pushing Brent above $110."
                ),
                probability=0.20,
                implications=(
                    "Headline inflation re-accelerates; emerging markets with "
                    "energy-import dependence face current-account pressure; "
                    "political pressure to release strategic reserves."
                ),
            ),
            Scenario(
                title="Cheating and Collapse",
                description=(
                    "Quota discipline breaks down within 60 days as members "
                    "cheat on production limits. Prices fall further."
                ),
                probability=0.25,
                implications=(
                    "OPEC+ credibility damaged; Gulf sovereigns face wider "
                    "fiscal deficits; US shale gains market share."
                ),
            ),
            Scenario(
                title="Demand Destruction",
                description=(
                    "Higher prices accelerate EV adoption and industrial "
                    "efficiency, structurally reducing oil demand growth."
                ),
                probability=0.20,
                implications=(
                    "Long-term bearish for crude; stranded-asset risk rises "
                    "for petrostates; green-transition equities rally."
                ),
            ),
        ],
        date="2026-04-11",
        region="Global",
    ),
    Event(
        id="spacex-starship-crewed-2026",
        title="SpaceX Crewed Starship Mission",
        category="tech",
        summary=(
            "SpaceX is preparing for the first crewed Starship orbital "
            "mission, a milestone that could reshape the economics of "
            "space access and accelerate lunar-return timelines."
        ),
        actors=["SpaceX", "NASA", "FAA", "ESA"],
        scenarios=[
            Scenario(
                title="Full Mission Success",
                description=(
                    "Starship completes a crewed orbital flight and returns "
                    "safely. NASA fast-tracks Artemis integration."
                ),
                probability=0.30,
                implications=(
                    "Space-economy valuations surge; launch-cost economics "
                    "disrupted; national space programs reassess vehicle "
                    "development strategies."
                ),
            ),
            Scenario(
                title="Partial Success",
                description=(
                    "Orbit is achieved but re-entry or landing encounters "
                    "issues. Crew is safe but program is delayed 6+ months."
                ),
                probability=0.35,
                implications=(
                    "Investor confidence dips temporarily; regulatory scrutiny "
                    "increases; competing programs get breathing room."
                ),
            ),
            Scenario(
                title="Abort / Scrub",
                description=(
                    "Technical or weather issues force repeated scrubs; mission "
                    "slips to late 2026."
                ),
                probability=0.25,
                implications=(
                    "Narrative setback but limited long-term impact; Artemis "
                    "timeline uncertainty grows."
                ),
            ),
            Scenario(
                title="Catastrophic Failure",
                description=(
                    "A launch or in-flight failure results in loss of vehicle. "
                    "Crew escape system is tested under real conditions."
                ),
                probability=0.10,
                implications=(
                    "Multi-year grounding; congressional hearings; commercial "
                    "space insurance premiums spike; public confidence shaken."
                ),
            ),
        ],
        date="2026-04-13",
        region="Global",
    ),
]

_INDEX = {e.id: e for e in EVENTS}


def get_events() -> list[Event]:
    """Return all events, newest first."""
    return sorted(EVENTS, key=lambda e: e.date, reverse=True)


def get_event_by_id(event_id: str) -> Event | None:
    return _INDEX.get(event_id)
