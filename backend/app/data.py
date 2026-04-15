"""Mock data for Foresight.

Replace this module with LLM-generated analysis by implementing a provider
that returns list[Event].  The rest of the app imports `get_events()` and
`get_event_by_id()` — swap the implementation without touching the API layer.
"""

from .models import ActorProfile, Event, Scenario, TimelineEntry

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
        id="iran-war-2026",
        title="US-Iran War: Day 46 — Blockade, Broken Ceasefire, and the April 21 Deadline",
        category="politics",
        summary=(
            "The US-Israel war on Iran is on Day 46. On February 28, the US and "
            "Israel launched coordinated strikes ('Operation Epic Fury' / "
            "'Operation Roaring Lion'), killing Supreme Leader Ali Khamenei and "
            "destroying nuclear and military sites. Iran retaliated with missiles "
            "on Israel and US bases, and closed the Strait of Hormuz. A fragile "
            "two-week ceasefire brokered by Pakistan took effect April 8, but "
            "21 hours of talks in Islamabad (Vance, Witkoff, Kushner vs. "
            "Araghchi, Ghalibaf) collapsed April 12 over Iran's refusal to "
            "abandon enrichment. Trump responded by ordering a naval blockade "
            "of all Iranian ports, now in effect. Oil is above $100/barrel. "
            "~20,000 vessels are stranded. The ceasefire expires April 21. "
            "Trump hints talks may resume in Pakistan within two days. "
            "Casualties: 3,375–7,650+ Iranian dead, 26,500 injured; 41 Israeli "
            "dead, 7,740 injured; 15 US soldiers killed, 538 wounded; 2,089+ "
            "dead in Lebanon. Economic damage to Iran: $270B–$1T."
        ),
        actors=[
            "Mojtaba Khamenei",
            "Masoud Pezeshkian",
            "Abbas Araghchi",
            "Donald Trump",
            "JD Vance",
            "Steve Witkoff",
            "Benjamin Netanyahu",
            "Shehbaz Sharif",
            "Xi Jinping",
        ],
        actor_profiles=[
            ActorProfile(
                name="Mojtaba Khamenei",
                role="Supreme Leader of Iran (since March 9, 2026)",
                public_position=(
                    "Vowed revenge on the US and Israel in his first statement "
                    "as Supreme Leader on March 12. Iran will never surrender "
                    "its nuclear sovereignty. The war was an act of unprovoked "
                    "aggression launched during active negotiations."
                ),
                likely_accepts=(
                    "An untested leader in an impossible position — his father "
                    "was assassinated by the countries he's negotiating with. "
                    "Reports in early April suggest he may be wounded or "
                    "incapacitated, raising questions about who actually holds "
                    "decision-making power. If functional, he needs a deal that "
                    "preserves the regime and can be framed as defiance, not "
                    "capitulation. Would likely accept a face-saving freeze on "
                    "enrichment with partial sanctions relief, but cannot be seen "
                    "as the leader who surrendered the program his father died "
                    "defending. The IRGC's influence over him is likely stronger "
                    "than it was over his father."
                ),
                incentives=[
                    "Regime survival — a new, untested Supreme Leader during an active war is maximally vulnerable",
                    "Consolidating personal authority over IRGC hardliners who may view him as a figurehead",
                    "Ending the blockade before it triggers another domestic uprising (Jan 2026 protests killed thousands)",
                    "Avenging his father's assassination is both personal and political — inaction weakens his legitimacy",
                    "Preventing the complete destruction of Iran's remaining nuclear and military infrastructure",
                ],
            ),
            ActorProfile(
                name="Masoud Pezeshkian",
                role="President of Iran",
                public_position=(
                    "Iran was attacked during good-faith negotiations — the US "
                    "and Israel committed an act of war while diplomats were at "
                    "the table in Geneva. Iran demands war reparations, security "
                    "guarantees, and recognition of its right to enrich uranium "
                    "for civilian purposes."
                ),
                likely_accepts=(
                    "The reformist president who wanted a deal before the war "
                    "now has far less room to maneuver. His credibility argument "
                    "— 'diplomacy works' — was shattered on Feb 28 when strikes "
                    "launched during active negotiations. Nonetheless, he is "
                    "Iran's most pragmatic senior voice. Would accept a "
                    "comprehensive ceasefire that includes: enrichment rights at "
                    "some level, phased sanctions relief, reconstruction aid, "
                    "and no regime-change language. Cannot accept anything that "
                    "looks like the terms of surrender."
                ),
                incentives=[
                    "Preventing total economic collapse — Iran has sustained $270B–$1T in damage",
                    "Reopening the Strait of Hormuz before the blockade destroys what's left of the economy",
                    "Restoring his reformist mandate by ending the war through diplomacy, not military escalation",
                    "Preventing hardliners from using the war to permanently sideline civilian government",
                ],
            ),
            ActorProfile(
                name="Abbas Araghchi",
                role="Foreign Minister of Iran, lead negotiator",
                public_position=(
                    "Iran negotiated in good faith across five rounds in 2025 "
                    "and two rounds in 2026 — the US responded by bombing "
                    "during the Geneva talks. Iran will not accept what amounts "
                    "to a surrender document. The nuclear program is a civilian "
                    "right under the NPT."
                ),
                likely_accepts=(
                    "The most experienced diplomat in the room and the only "
                    "Iranian official who has been present across all nine "
                    "rounds of talks. Personally committed to a negotiated "
                    "outcome. Would accept: enrichment capped below weapons-grade "
                    "with IAEA monitoring, phased sanctions relief on a clear "
                    "timeline, Hormuz reopened as part of a package, and "
                    "exclusion of missiles and proxies from the nuclear deal "
                    "scope. His red line: no dismantlement of enrichment "
                    "capability and no transfer of uranium stockpiles abroad."
                ),
                incentives=[
                    "Professional legacy — has been central to Iran's nuclear diplomacy for over a decade",
                    "Preventing the collapse of the ceasefire before April 21",
                    "Demonstrating to the IRGC that diplomacy can secure better terms than continued war",
                    "Keeping Iran's international standing from complete isolation",
                ],
            ),
            ActorProfile(
                name="Donald Trump",
                role="President of the United States",
                public_position=(
                    "The strikes were necessary to prevent a nuclear Iran. "
                    "Iran's infrastructure will be 'blown to hell' if they "
                    "don't make a deal. The Hormuz blockade will force Iran "
                    "to the table. Open to the 'biggest deal ever' if Iran "
                    "commits to full denuclearization."
                ),
                likely_accepts=(
                    "Ordered the war but now needs to end it — oil at $100+ "
                    "is a domestic political crisis. Hinted April 14 that "
                    "talks could resume within days. In practice, would likely "
                    "accept a deal that falls short of full dismantlement if "
                    "it includes: visible destruction of some enrichment "
                    "infrastructure he can show on TV, Iran's verbal commitment "
                    "to not pursue weapons, and a signing ceremony he can brand "
                    "as historic. Less interested in verification details than "
                    "in the optics. The blockade is both leverage and a trap — "
                    "if it doesn't produce a deal quickly, the economic "
                    "blowback to the US and allies grows."
                ),
                incentives=[
                    "Ending the war with a 'win' narrative before economic damage deepens at home",
                    "Oil prices above $100 are a direct threat to his domestic approval and midterm prospects",
                    "20,000 stranded vessels and allied pressure to reopen Hormuz — the blockade has a shelf life",
                    "Wants to be the president who solved the Iran problem, not the one who started an endless war",
                    "Balancing hawks in his administration (Hegseth) who want continued strikes against economic reality",
                ],
            ),
            ActorProfile(
                name="JD Vance",
                role="Vice President of the United States, led Islamabad delegation",
                public_position=(
                    "The US needs 'an affirmative commitment that Iran will "
                    "not seek a nuclear weapon and will not seek the tools "
                    "that would enable them to quickly achieve one.' Left "
                    "Islamabad saying talks ended without agreement."
                ),
                likely_accepts=(
                    "Vance led the 21-hour Islamabad marathon and has the most "
                    "granular view of where the gaps are. His public framing — "
                    "'tools to quickly achieve a weapon' — is softer than full "
                    "dismantlement and may signal the actual US bottom line: "
                    "enrichment caps well below weapons-grade with intrusive "
                    "verification, rather than zero enrichment. He is the key "
                    "conduit between Trump and the negotiating details."
                ),
                incentives=[
                    "Political positioning for a future presidential run — being 'the man who ended the Iran war'",
                    "Demonstrating diplomatic competence after inheriting a war he didn't start",
                    "Managing the gap between Trump's maximalist rhetoric and achievable deal terms",
                ],
            ),
            ActorProfile(
                name="Steve Witkoff",
                role="Special Envoy, lead US negotiator since 2025",
                public_position=(
                    "The US has been consistent in its demands. Iran must "
                    "dismantle its enrichment program, destroy facilities at "
                    "Fordow, Natanz, and Isfahan, and transfer stockpiles to "
                    "third countries."
                ),
                likely_accepts=(
                    "The only US official who has been across all rounds of "
                    "talks from April 2025 through Islamabad. Understands the "
                    "technical details better than anyone in the US delegation. "
                    "Has privately navigated the gap between Trump's public "
                    "maximalism and the need for a workable agreement. His "
                    "presence in a second round would signal the US is serious "
                    "about bridging the gap before April 21."
                ),
                incentives=[
                    "Personal legacy as the envoy who brokered an end to the war",
                    "Institutional credibility — repeated failures damage the envoy's position",
                    "Pragmatic interest in a deal that actually holds, not just a signing ceremony",
                ],
            ),
            ActorProfile(
                name="Benjamin Netanyahu",
                role="Prime Minister of Israel",
                public_position=(
                    "Operation Roaring Lion was a pre-emptive strike to prevent "
                    "an existential threat. Israel will continue to act to "
                    "protect its security. Denies that Lebanon was included in "
                    "the ceasefire — continued strikes in Lebanon after April 8."
                ),
                likely_accepts=(
                    "Has already achieved his primary objective: Iran's nuclear "
                    "infrastructure is severely degraded and Khamenei is dead. "
                    "Now wants to lock in the gains through a deal that "
                    "permanently caps Iran's enrichment capability. The Lebanon "
                    "front is his secondary objective — continued strikes on "
                    "Hezbollah are an attempt to reshape the regional balance "
                    "while the window is open. Would accept a deal that keeps "
                    "Iran's breakout time at 2+ years with permanent IAEA "
                    "presence and an end to Iranian support for Hezbollah."
                ),
                incentives=[
                    "Consolidating the military gains before international pressure forces a premature ceasefire",
                    "Using the Lebanon ambiguity in the ceasefire to continue degrading Hezbollah",
                    "Securing a US mutual defense treaty as part of the broader deal",
                    "Legacy: 'the PM who destroyed Iran's nuclear program and eliminated Khamenei'",
                    "Domestic political survival — must deliver permanent security, not just a pause",
                ],
            ),
            ActorProfile(
                name="Shehbaz Sharif",
                role="Prime Minister of Pakistan, ceasefire mediator",
                public_position=(
                    "Pakistan is an honest broker seeking peace. The ceasefire "
                    "covers all fronts. Both sides must return to the table "
                    "before April 21."
                ),
                likely_accepts=(
                    "Pakistan brokered the ceasefire and hosted the Islamabad "
                    "talks — its credibility is on the line. Army Chief Asim "
                    "Munir is the behind-the-scenes power in the mediation. "
                    "Pakistan's unique position: a nuclear-armed Muslim-majority "
                    "state with ties to both the US and Iran, and historical "
                    "nuclear cooperation with Saudi Arabia. Needs the ceasefire "
                    "to hold and convert into permanent talks — a collapse would "
                    "damage Pakistan's standing and risk spillover instability."
                ),
                incentives=[
                    "International prestige as the mediator who brokered a major war ceasefire",
                    "Preventing regional instability from spilling into Pakistan's Balochistan border region",
                    "Strengthening ties with both the US and Gulf states through successful mediation",
                    "Distancing Pakistan from its image as a crisis state — rebranding as a diplomatic power",
                ],
            ),
            ActorProfile(
                name="Xi Jinping",
                role="President of China",
                public_position=(
                    "The US blockade of the Strait of Hormuz is a 'dangerous "
                    "and irresponsible act' that will further inflame tensions. "
                    "China opposes the use of force and calls for immediate "
                    "de-escalation."
                ),
                likely_accepts=(
                    "China is the most affected bystander. The Hormuz closure "
                    "has disrupted 40% of China's oil imports, and the US "
                    "blockade directly threatens Chinese-flagged vessels. "
                    "Beijing's calculus has shifted from passive beneficiary "
                    "of cheap Iranian crude to active damage control. Would "
                    "accept any deal that reopens Hormuz immediately. May be "
                    "willing to pressure Iran privately in exchange for US "
                    "concessions elsewhere (tariffs, Taiwan). The longer the "
                    "blockade lasts, the more likely China intervenes "
                    "diplomatically — or escalates its own naval presence."
                ),
                incentives=[
                    "Reopening the Strait of Hormuz is an urgent national security priority — energy prices are spiking domestically",
                    "Preventing the US from establishing a precedent of unilateral naval blockades in critical waterways",
                    "Protecting ~$30B in annual Chinese-Iranian trade and Belt and Road investments",
                    "Leveraging the crisis for concessions from the US on trade, Taiwan, or tech restrictions",
                    "Avoiding a scenario where the US blockade succeeds and validates maximum pressure as a doctrine",
                ],
            ),
        ],
        timeline=[
            TimelineEntry(
                date="2026-02-28",
                label="US-Israel Strikes Begin",
                description="Operation Epic Fury / Roaring Lion. Khamenei killed. 500+ targets hit in 24 hours.",
            ),
            TimelineEntry(
                date="2026-03-09",
                label="Mojtaba Khamenei Named Supreme Leader",
                description="Assembly of Experts elects Khamenei's son. Controversial dynastic succession.",
            ),
            TimelineEntry(
                date="2026-03-12",
                label="New Leader Vows Revenge",
                description="Mojtaba's first public statement pledges retaliation against the US and Israel.",
            ),
            TimelineEntry(
                date="2026-03-27",
                label="Israel Strikes Nuclear Sites",
                description="Second wave targets Natanz, Fordow, and Isfahan enrichment facilities.",
            ),
            TimelineEntry(
                date="2026-04-08",
                label="Pakistan-Brokered Ceasefire",
                description="Two-week ceasefire takes effect. Dispute over whether Lebanon is included.",
            ),
            TimelineEntry(
                date="2026-04-12",
                label="Islamabad Talks Collapse",
                description="21-hour marathon ends without agreement. Vance leaves Pakistan. Nuclear enrichment is the sticking point.",
            ),
            TimelineEntry(
                date="2026-04-13",
                label="US Naval Blockade Begins",
                description="Trump orders blockade of all Iranian ports. Oil surges above $100. ~20,000 vessels stranded.",
            ),
            TimelineEntry(
                date="2026-04-14",
                label="Day 46 — Today",
                description="Trump hints talks may resume within days. China calls blockade 'dangerous and irresponsible.'",
            ),
            TimelineEntry(
                date="2026-04-21",
                label="Ceasefire Expires",
                description="Two-week ceasefire deadline. No extension agreed. Risk of resumed hostilities.",
            ),
        ],
        deadline="2026-04-21",
        deadline_label="Ceasefire expires",
        featured=True,
        scenarios=[
            Scenario(
                title="Second Round of Talks Produces Framework Before April 21",
                description=(
                    "Trump's hint of resumed talks materializes. A second round "
                    "in Islamabad or a neutral venue produces a framework: Iran "
                    "accepts enrichment caps at 20% (well below weapons-grade) "
                    "with enhanced IAEA monitoring. The US lifts the naval "
                    "blockade and agrees to phased sanctions relief. Hormuz "
                    "reopens. Nuclear dismantlement is deferred to a 'Phase 2' "
                    "that may never happen. Ceasefire is extended indefinitely."
                ),
                probability=0.20,
                implications=(
                    "Oil drops 15–20% within days as Hormuz reopens. Global "
                    "recession fears ease. Both sides claim victory — Trump "
                    "calls it 'the greatest deal in history,' Iran frames the "
                    "enrichment cap as a sovereign choice, not a concession. "
                    "Israel is unhappy but acquiesces. The underlying issues "
                    "(missiles, proxies, reconstruction) remain unresolved. "
                    "Fragile but functional."
                ),
            ),
            Scenario(
                title="Ceasefire Expires, War Resumes with Escalation",
                description=(
                    "No second round materializes. April 21 passes without "
                    "extension. Trump orders strikes on Iranian infrastructure "
                    "targets he previously threatened. Iran retaliates against "
                    "US bases and Gulf shipping. Hezbollah opens a full second "
                    "front against Israel. The Hormuz closure becomes a "
                    "military confrontation, not just a blockade."
                ),
                probability=0.20,
                implications=(
                    "Oil surges past $130. Global recession becomes near-certain. "
                    "20,000+ stranded vessels become a humanitarian crisis. US "
                    "allies (Japan, South Korea, Europe) face acute energy "
                    "shortages. Domestic anti-war pressure grows in the US. "
                    "Casualty counts on all sides escalate sharply. "
                    "Intervention by China or Russia becomes more likely."
                ),
            ),
            Scenario(
                title="Ceasefire Extended But No Deal — Frozen Conflict",
                description=(
                    "Both sides agree to extend the ceasefire 30–90 days to "
                    "continue negotiations, but neither makes real concessions. "
                    "The blockade is partially eased to allow humanitarian "
                    "shipping. A grinding status quo sets in — no peace, no "
                    "war, no resolution. Talks continue intermittently."
                ),
                probability=0.30,
                implications=(
                    "Oil stabilizes in the $90–100 range — elevated but not "
                    "crisis-level. Markets adapt to a new normal of Hormuz "
                    "risk premium. Iran's economy deteriorates steadily. "
                    "Reconstruction is impossible without sanctions relief. "
                    "Both sides use the pause to rearm. The conflict becomes "
                    "the Middle East's new frozen war, like Korea after 1953."
                ),
            ),
            Scenario(
                title="China Brokers a Parallel Deal",
                description=(
                    "Beijing, facing acute energy disruption, intervenes "
                    "diplomatically with an offer: China guarantees Iranian "
                    "oil purchases and reconstruction funding in exchange for "
                    "Iran accepting enrichment limits and reopening Hormuz. "
                    "China pressures the US to accept by threatening to "
                    "escalate its naval presence in the Gulf."
                ),
                probability=0.15,
                implications=(
                    "A geopolitical earthquake. China displaces the US as the "
                    "primary diplomatic power in the Gulf. Iran becomes a "
                    "Chinese client state. US influence in the Middle East "
                    "declines permanently. Oil flows resume but through "
                    "Chinese-dominated channels. Gulf states hedge toward "
                    "Beijing. The petrodollar system faces its most serious "
                    "challenge."
                ),
            ),
            Scenario(
                title="Iranian Regime Fracture Under Pressure",
                description=(
                    "The combination of Khamenei's assassination, Mojtaba's "
                    "possible incapacitation, economic collapse, and military "
                    "devastation triggers an internal power struggle. IRGC "
                    "hardliners attempt to sideline Pezeshkian and the "
                    "diplomats. Either a military junta emerges or the regime "
                    "fragments, creating chaos but also an opening for a "
                    "fundamentally different deal."
                ),
                probability=0.15,
                implications=(
                    "Maximum uncertainty. A military junta could escalate "
                    "unpredictably or, conversely, a pragmatic general could "
                    "cut a deal the clerics never would. Regime collapse risks "
                    "loose nuclear material — a nightmare scenario for all "
                    "parties. Regional proxy networks lose central coordination. "
                    "Humanitarian crisis deepens. The 'be careful what you wish "
                    "for' scenario for regime-change advocates."
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
