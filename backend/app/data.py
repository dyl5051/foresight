"""Mock data for Foresight.

Replace this module with LLM-generated analysis by implementing a provider
that returns list[Event].  The rest of the app imports `get_events()` and
`get_event_by_id()` — swap the implementation without touching the API layer.
"""

from .models import ActorProfile, Event, Scenario

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
    Event(
        id="iran-nuclear-crisis-2026",
        title="Iran Nuclear Crisis: Diplomacy, Strikes, and the Brink",
        category="politics",
        summary=(
            "Tensions over Iran's nuclear program have reached their highest "
            "point since 2012. IAEA inspectors report Iran has enriched uranium "
            "to 84% purity — a short technical step from weapons-grade 90%. "
            "The US and Israel have signaled that the window for diplomacy is "
            "closing, while Iran insists its program is peaceful and demands "
            "sanctions relief as a precondition for talks. Russia and China "
            "have blocked further UN Security Council action, and Gulf states "
            "are quietly pursuing their own hedging strategies. Back-channel "
            "negotiations via Oman are reportedly underway, but public rhetoric "
            "on all sides is escalating."
        ),
        actors=[
            "Ali Khamenei",
            "Masoud Pezeshkian",
            "Donald Trump",
            "Benjamin Netanyahu",
            "Vladimir Putin",
            "Xi Jinping",
            "Mohammed bin Salman",
            "Rafael Grossi",
        ],
        actor_profiles=[
            ActorProfile(
                name="Ali Khamenei",
                role="Supreme Leader of Iran",
                public_position=(
                    "Nuclear weapons are forbidden by Islamic decree (fatwa). "
                    "Iran's enrichment is for energy and medical isotopes. "
                    "Any attack on Iranian soil will be met with devastating "
                    "retaliation across the region."
                ),
                likely_accepts=(
                    "A face-saving deal that lifts oil and banking sanctions "
                    "in exchange for enrichment caps at 60% and enhanced IAEA "
                    "monitoring — but not full dismantlement. Needs to frame "
                    "any agreement as Iran negotiating from strength, not "
                    "capitulation. Would likely accept freezing at 60% if the "
                    "IRGC is not designated as a terrorist organization and "
                    "Iran's regional influence is not on the table."
                ),
                incentives=[
                    "Regime survival is the paramount concern — everything else is subordinate",
                    "Sanctions relief to quell domestic economic discontent and prevent another 2019-style uprising",
                    "Maintaining the nuclear hedge as a strategic deterrent without crossing the threshold that triggers a strike",
                    "Preserving Iran's regional proxy network (Hezbollah, Houthis, Iraqi militias) as asymmetric leverage",
                    "Legacy: does not want to be the leader who either lost the program or triggered a devastating war",
                ],
            ),
            ActorProfile(
                name="Masoud Pezeshkian",
                role="President of Iran",
                public_position=(
                    "Iran is ready for diplomacy and has always been open to "
                    "negotiations. The West must first return to its JCPOA "
                    "commitments. Sanctions are economic warfare against the "
                    "Iranian people."
                ),
                likely_accepts=(
                    "Genuinely wants a deal to deliver economic relief and "
                    "consolidate his reformist base. Would accept significant "
                    "nuclear constraints if packaged as a 'new JCPOA' rather "
                    "than a concession. His room to maneuver depends entirely "
                    "on Khamenei's green light — he can negotiate the details "
                    "but not the red lines."
                ),
                incentives=[
                    "Economic recovery to validate his election — GDP contraction and 40%+ inflation undermine his mandate",
                    "Building political capital vs. hardliners by delivering tangible results",
                    "Opening Iran to foreign investment, especially in oil/gas infrastructure",
                    "Demonstrating that reformists can achieve what hardliners could not",
                ],
            ),
            ActorProfile(
                name="Donald Trump",
                role="President of the United States",
                public_position=(
                    "Iran will never have a nuclear weapon on his watch. "
                    "Maximum pressure works. Open to the 'biggest deal ever' "
                    "if Iran agrees to full denuclearization, missile limits, "
                    "and ending support for proxies."
                ),
                likely_accepts=(
                    "A grand photo-op deal that he can brand as superior to "
                    "the JCPOA. In practice, would likely accept a freeze at "
                    "current enrichment levels with enhanced inspections if it "
                    "comes with visible Iranian concessions on missiles or "
                    "proxies he can sell domestically. Less interested in "
                    "technical nuclear details than in the optics of a "
                    "historic agreement. Would accept something substantively "
                    "similar to the JCPOA if it has his name on it."
                ),
                incentives=[
                    "A legacy-defining foreign policy 'win' — the deal-maker narrative",
                    "Preventing a war that could spike oil prices before midterms",
                    "Outflanking hawkish advisors who push for strikes while retaining their support",
                    "Keeping oil prices low to support domestic economic messaging",
                    "Demonstrating unpredictability as a negotiating asset",
                ],
            ),
            ActorProfile(
                name="Benjamin Netanyahu",
                role="Prime Minister of Israel",
                public_position=(
                    "A nuclear Iran is an existential threat to Israel. All "
                    "options are on the table. Any deal that leaves Iran with "
                    "enrichment capability is unacceptable. Israel will act "
                    "alone if necessary."
                ),
                likely_accepts=(
                    "Privately, a deal that pushes Iran's breakout time back "
                    "to 6+ months with intrusive inspections would be "
                    "grudgingly tolerable — though he would never say so "
                    "publicly. A limited military strike on nuclear facilities "
                    "(Natanz, Fordow) is his preferred outcome if diplomacy "
                    "fails, but only with US logistical support or at minimum "
                    "tacit approval. Does not want a full-scale regional war "
                    "that draws in Hezbollah and risks Israeli home-front "
                    "casualties."
                ),
                incentives=[
                    "Political survival — coalition depends on projecting strength on Iran",
                    "Diverting attention from domestic legal troubles and governance crises",
                    "Establishing a security legacy: 'the PM who neutralized the Iranian nuclear threat'",
                    "Maintaining Israel's regional military superiority and nuclear monopoly in the Middle East",
                    "Leveraging the Iran threat to deepen Abraham Accords and Gulf security partnerships",
                ],
            ),
            ActorProfile(
                name="Vladimir Putin",
                role="President of Russia",
                public_position=(
                    "Supports Iran's right to peaceful nuclear energy. "
                    "Opposes unilateral sanctions and military threats. "
                    "Calls for a return to multilateral diplomacy within "
                    "the JCPOA framework."
                ),
                likely_accepts=(
                    "Happy with managed tension that keeps the US distracted "
                    "and oil prices elevated. Would support a deal only if "
                    "Russia is at the table and gets credit as a mediator. "
                    "Does not actually want Iran to get a weapon — a nuclear "
                    "Iran would be an unpredictable neighbor — but will block "
                    "Western-led pressure as long as it serves Russian "
                    "interests in the broader US confrontation."
                ),
                incentives=[
                    "High oil prices directly fund Russia's war economy and budget",
                    "US strategic attention on Iran means less bandwidth for Ukraine and NATO expansion",
                    "Arms sales and nuclear-plant contracts with Iran (Bushehr)",
                    "Positioning Russia as an indispensable diplomatic player",
                    "Preventing a precedent where Western pressure forces denuclearization (implications for Russia's own posture)",
                ],
            ),
            ActorProfile(
                name="Xi Jinping",
                role="President of China",
                public_position=(
                    "China opposes nuclear proliferation but also opposes "
                    "unilateral sanctions and the use of force. Supports "
                    "dialogue and the JCPOA framework."
                ),
                likely_accepts=(
                    "Will continue buying Iranian oil at a discount regardless "
                    "of sanctions. Prefers a low-boil crisis that doesn't "
                    "disrupt Strait of Hormuz shipping or force China to pick "
                    "sides publicly. Would accept any deal that stabilizes "
                    "the region and keeps oil flowing, but won't spend "
                    "political capital to make one happen."
                ),
                incentives=[
                    "Discounted Iranian crude — China imports ~1.5M barrels/day from Iran, essential for energy security",
                    "Strait of Hormuz stability — 40% of China's oil imports transit the strait",
                    "Avoiding a precedent where US maximum pressure works (implications for Taiwan)",
                    "Belt and Road investments in Iran and the broader Middle East corridor",
                    "Maintaining strategic ambiguity as leverage with both the US and Iran",
                ],
            ),
            ActorProfile(
                name="Mohammed bin Salman",
                role="Crown Prince of Saudi Arabia",
                public_position=(
                    "Saudi Arabia seeks regional stability and supports a "
                    "diplomatic solution. Has stated that if Iran gets a "
                    "nuclear weapon, Saudi Arabia will acquire one as well."
                ),
                likely_accepts=(
                    "Privately prefers a US or Israeli strike that degrades "
                    "Iran's capabilities without Saudi fingerprints. If a deal "
                    "is reached, wants equivalent nuclear rights (enrichment "
                    "for civilian purposes) and a US security guarantee. "
                    "The 2023 China-brokered Saudi-Iran détente was tactical, "
                    "not a fundamental realignment — MBS still views Iran as "
                    "the primary regional rival."
                ),
                incentives=[
                    "Preventing an Iranian bomb that would end Saudi Arabia's conventional military superiority",
                    "Securing US nuclear-cooperation agreement (123 agreement) with enrichment rights",
                    "Vision 2030 requires regional stability and foreign investment confidence",
                    "Maintaining leverage in the Abraham Accords / normalization track with Israel",
                    "Oil price stability — a Hormuz crisis helps short-term revenue but destroys long-term demand",
                ],
            ),
            ActorProfile(
                name="Rafael Grossi",
                role="Director General of the IAEA",
                public_position=(
                    "Iran must provide full transparency to inspectors. The "
                    "IAEA has detected particles at 83.7% enrichment. "
                    "Calls on all parties to preserve the verification "
                    "framework."
                ),
                likely_accepts=(
                    "Needs any deal to include IAEA access to all declared "
                    "and suspected sites, continuous monitoring, and "
                    "resolution of outstanding questions about undeclared "
                    "nuclear material. Personally invested in being the "
                    "diplomat who keeps the verification architecture intact "
                    "through the crisis."
                ),
                incentives=[
                    "Institutional credibility — the IAEA's relevance depends on being the trusted verification body",
                    "Preventing a precedent where a state enriches to near-weapons-grade without consequences",
                    "Personal legacy as the DG who navigated the most dangerous nuclear crisis since North Korea",
                    "Maintaining access — even limited monitoring is better than Iran expelling inspectors entirely",
                ],
            ),
        ],
        scenarios=[
            Scenario(
                title="Back-Channel Deal via Oman",
                description=(
                    "Secret negotiations through Muscat produce a framework: "
                    "Iran freezes enrichment at 60%, accepts enhanced IAEA "
                    "monitoring including cameras at Fordow, and receives "
                    "phased sanctions relief on oil exports and central bank "
                    "access. The US rebrands it as a new agreement distinct "
                    "from the JCPOA. Israel protests but acquiesces after "
                    "receiving US commitments on a mutual defense treaty."
                ),
                probability=0.20,
                implications=(
                    "Oil prices drop 8–12% on supply expectations; Iranian "
                    "rial stabilizes; Gulf states demand matching nuclear "
                    "rights; Israel-US relations strained but manageable; "
                    "regional proxy networks remain intact, setting up future "
                    "friction. Biggest winner: Iranian reformists. Biggest "
                    "loser: Israeli hawks."
                ),
            ),
            Scenario(
                title="Israeli Targeted Strike on Nuclear Facilities",
                description=(
                    "Israel conducts a multi-wave air and cyber operation "
                    "against Natanz and Fordow enrichment sites, using "
                    "bunker-busting munitions. The US is informed hours "
                    "beforehand but does not participate directly. Iran's "
                    "enrichment capability is set back 2–3 years but not "
                    "permanently destroyed. Iran retaliates via Hezbollah "
                    "rocket barrages and Houthi attacks on Gulf shipping."
                ),
                probability=0.25,
                implications=(
                    "Oil spikes above $120 within days; global recession risk "
                    "rises sharply; Strait of Hormuz insurance premiums "
                    "skyrocket; Iran fully expels IAEA inspectors and "
                    "reconstitutes a covert program; regional war risk "
                    "escalates for 3–6 months before a grinding stalemate. "
                    "Biggest winner: nobody. Biggest loser: global economy "
                    "and Iranian civilians."
                ),
            ),
            Scenario(
                title="Managed Ambiguity / Status Quo Drift",
                description=(
                    "No deal and no strike. Iran remains at 84% enrichment "
                    "but doesn't cross to 90%. The IAEA maintains minimal "
                    "monitoring. Sanctions continue but are widely evaded "
                    "via Chinese and Russian channels. Everyone pretends the "
                    "situation is sustainable."
                ),
                probability=0.30,
                implications=(
                    "Markets price in a permanent risk premium on Gulf oil; "
                    "Saudi Arabia accelerates its own nuclear program; "
                    "Iran's economy stagnates but doesn't collapse; Israel "
                    "maintains strike readiness as a permanent posture; "
                    "NPT regime erodes as other states conclude enrichment "
                    "to near-weapons-grade has no consequences. This is the "
                    "most likely outcome precisely because it requires no "
                    "actor to make a hard choice."
                ),
            ),
            Scenario(
                title="Iranian Nuclear Breakout",
                description=(
                    "Iran expels remaining IAEA inspectors and enriches to "
                    "90% at Fordow (deep underground, hard to strike). "
                    "Within 3–6 months, US intelligence assesses Iran has "
                    "enough fissile material for 1–2 devices. Iran does not "
                    "test but maintains deliberate ambiguity."
                ),
                probability=0.15,
                implications=(
                    "Middle East enters a nuclear-arms race: Saudi Arabia "
                    "activates Pakistani warhead arrangements, Turkey and "
                    "Egypt reconsider their options. US credibility on "
                    "nonproliferation collapses. Oil markets enter sustained "
                    "crisis pricing. Israel faces an existential strategic "
                    "dilemma between striking a nuclear-armed state and "
                    "accepting deterrence."
                ),
            ),
            Scenario(
                title="US-Led Maximum Pressure Collapse of Iran's Economy",
                description=(
                    "The US successfully pressures China to reduce Iranian "
                    "oil purchases (via secondary sanctions on Chinese banks), "
                    "cratering Iran's remaining export revenue. Domestic "
                    "unrest flares. The regime cracks down violently but "
                    "eventually returns to negotiations from a position of "
                    "weakness."
                ),
                probability=0.10,
                implications=(
                    "A deal under duress is fragile and breeds revanchism. "
                    "China-US relations further deteriorate over secondary "
                    "sanctions. Iranian hardliners are either empowered by "
                    "nationalist backlash or sidelined by economic desperation. "
                    "Humanitarian crisis worsens. Oil markets volatile but "
                    "ultimately bearish as Iranian capitulation is priced in."
                ),
            ),
        ],
        date="2026-04-14",
        region="Middle East",
    ),
]

_INDEX = {e.id: e for e in EVENTS}


def get_events() -> list[Event]:
    """Return all events, newest first."""
    return sorted(EVENTS, key=lambda e: e.date, reverse=True)


def get_event_by_id(event_id: str) -> Event | None:
    return _INDEX.get(event_id)
