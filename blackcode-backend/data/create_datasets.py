import csv
import os

# Define the columns exactly as required
columns = [
    "provision_id", "source_type", "part_chapter", "article_section", "title",
    "verbatim_text_excerpt", "simplified_explanation", "keywords", "landmark_case_1",
    "lc1_year", "lc1_holding_summary", "landmark_case_2", "lc2_year", "lc2_holding_summary",
    "upsc_relevance", "category", "enforcement_year", "nodal_ministry", "legal_classification",
    "punishment_quantum", "exceptions_and_limitations", "cross_references", "bench_strength",
    "current_precedent_status", "primary_source_url", "current_law_mapping", "row_status"
]

bns_rows = [
    [
        "BNS-001", "Statute", "Chapter I - Preliminary", "Section 4", "General Explanations and Definitions in BNS",
        "Words and expressions used in this Sanhita shall be interpreted according to their definitions. Gender includes all genders. Person includes association of individuals.",
        "Section 4 of BNS (formerly Section 11 of IPC) defines general terms. 'Person' includes any company or association or body of persons, whether incorporated or not. 'Gender' includes male, female, and transgender individuals. 'Public' includes any class of the public or any community.",
        "BNS Section 4, Definitions, Person, Gender, Public, General Explanations, IPC 11",
        "State of Bihar v. Sm. Charusila Dasi", 1959,
        "The definition of person is wide enough to include juridical persons such as deities, trusts, and corporations.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Medium", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable depending on the specific offense context",
        "Not Applicable / N.A.", "Subject to constitutional limitations.", "Not Applicable / N.A.",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-002", "Statute", "Chapter IV - Abetment, Criminal Conspiracy and Attempt", "Section 61", "Criminal Conspiracy in BNS",
        "When two or more persons agree to do, or cause to be done - (a) an illegal act; or (b) an act which is not illegal by illegal means, such an agreement is designated a criminal conspiracy.",
        "Section 61 of BNS (formerly Section 120A of IPC) defines Criminal Conspiracy. It requires an agreement between two or more people to commit an illegal act, or a legal act by illegal means. For offenses other than serious crimes, some overt act must be done to show the conspiracy.",
        "BNS Section 61, Criminal Conspiracy, Agreement, Illegal Act, IPC 120A, IPC 120B",
        "State (NCT of Delhi) v. Navjot Sandhu", 2005,
        "Conspiracy is mostly proved by circumstantial evidence, as agreements are made in secrecy; direct evidence is rarely available.",
        "Topandas v. State of Bombay", 1956, "One person alone cannot be convicted of conspiracy unless others are also conspirators.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable if the offense conspired is cognizable",
        "As specified in Section 61(2) BNS", "Not Applicable / N.A.", "Section 61(2) BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-003", "Statute", "Chapter V - Offences Against Woman and Child", "Section 63", "Rape under BNS",
        "A man is said to commit rape who has sexual intercourse with a woman against her will, without her consent, or when consent is obtained by putting her in fear of death or hurt.",
        "Section 63 of BNS (replaces Section 375 of IPC) defines rape. It involves sexual intercourse without the woman's consent or against her will, including consent obtained by threat or fraud. The age of consent is 18 years. Marital rape remains exempt if the wife is not under 18 years.",
        "BNS Section 63, Rape, Consent, Sexual Assault, IPC 375, IPC 376",
        "State of Punjab v. Gurmit Singh", 1996,
        "The testimony of a rape survivor is vital and does not require corroboration if it inspires confidence.",
        "Independent Thought v. Union of India", 2017, "Sexual intercourse by a man with his wife, who is under 18 years of age, is rape.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Rigorous imprisonment of not less than 10 years, which may extend to life imprisonment, and fine.",
        "Marital rape exception (where wife is not under 18 years of age).", "Section 64 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-004", "Statute", "Chapter V - Offences Against Woman and Child", "Section 70", "Gang Rape under BNS",
        "Where a woman is raped by one or more persons constituting a group or acting in furtherance of a common intention, each of those persons shall be deemed to have committed gang rape.",
        "Section 70 of BNS (formerly Section 376D of IPC) governs gang rape. When a group of persons commits rape, every person involved is deemed guilty of gang rape and punished with rigorous imprisonment of not less than 20 years, which can extend to life (meaning remainder of natural life), or death if the victim is under 12 or 16 in specific variants.",
        "BNS Section 70, Gang Rape, S.70 BNS, IPC 376D, Common Intention",
        "State of Karnataka v. Raju", 2007,
        "In gang rape, even if some members of the group did not perform the actual sexual act, they are liable if they shared the common intention and aided the crime.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Rigorous imprisonment of not less than 20 years up to imprisonment for remainder of natural life, or death for minor victims under Section 70(2).",
        "Subject to judicial discretion.", "Section 63 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-005", "Statute", "Chapter V - Offences Against Woman and Child", "Section 74", "Assault with Intent to Outrage Modesty",
        "Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty, shall be punished.",
        "Section 74 of BNS (formerly Section 354 of IPC) punishes anyone who uses criminal force or assaults a woman with the intent or knowledge that it will outrage her modesty. It is a cognizable offense with a punishment of 1 to 5 years of imprisonment and fine.",
        "BNS Section 74, Outraging Modesty, Criminal Force, S.74 BNS, IPC 354",
        "State of Punjab v. Major Singh", 1967,
        "Modesty is an attribute associated with female human beings as a class, regardless of age; even a sleeping child or infant has modesty.",
        "Rupan Deol Bajaj v. K.P.S. Gill", 1995, "Modesty is outranked or outraged if the act of the offender is such that it would be shocking to the sense of decency of a woman.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Imprisonment of 1 to 5 years and fine.",
        "Subject to judicial evaluation of facts.", "Section 75 BNS, Section 78 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-006", "Statute", "Chapter V - Offences Against Woman and Child", "Section 75", "Sexual Harassment under BNS",
        "A man committing physical contact and advances involving unwelcome and explicit sexual overtures, or demanding or requesting sexual favours, or showing pornography against her will, or making sexually coloured remarks, shall be guilty of the offence of sexual harassment.",
        "Section 75 of BNS (formerly Section 354A of IPC) codifies sexual harassment. It includes physical contact, demanding sexual favors, showing pornography, or making sexually colored remarks. Punishments vary from 1 to 3 years of imprisonment depending on the subsection.",
        "BNS Section 75, Sexual Harassment, Physical Contact, Sexual Favours, Pornography, IPC 354A",
        "Vishaka v. State of Rajasthan", 1997,
        "Laid down extensive guidelines to prevent sexual harassment at workplaces, which led to the POSH Act and codification in criminal law.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Bailable (except specific subsets which are non-bailable)",
        "Rigorous imprisonment up to 3 years, or simple imprisonment up to 1 year, or fine, or both.",
        "Must be unwelcome and explicit behavior.", "POSH Act 2013",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-007", "Statute", "Chapter V - Offences Against Woman and Child", "Section 77", "Voyeurism under BNS",
        "Any man who watches, or captures the image of a woman engaging in a private act in circumstances where she would usually have the expectation of not being observed, or disseminates such image, shall be punished.",
        "Section 77 of BNS (formerly Section 354C of IPC) criminalizes voyeurism. It punishes watching, photographing, or filming a woman in a private space (like changing rooms, washrooms) without consent, or sharing those images. First conviction is bailable, second is non-bailable.",
        "BNS Section 77, Voyeurism, Hidden Camera, Private Act, IPC 354C",
        "State of West Bengal v. Anirban Chakraborty", 2018,
        "Admissibility of digital evidence and protection of privacy of the victim are crucial in voyeurism and cyber-crime trials.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Medium", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Bailable for first offense (Non-bailable for subsequent convictions)",
        "Imprisonment of 1 to 3 years for first offense; 3 to 7 years for second offense, along with fine.",
        "Expectation of privacy must exist in the circumstances.", "Information Technology Act 2000 Section 66E",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-008", "Statute", "Chapter V - Offences Against Woman and Child", "Section 78", "Stalking under BNS",
        "Any man who follows a woman and contacts, or attempts to contact such woman to foster personal interaction repeatedly despite a clear indication of disinterest by such woman; or monitors the use by a woman of the internet, email or any other form of electronic communication, commits stalking.",
        "Section 78 of BNS (formerly Section 354D of IPC) criminalizes stalking. It covers following a woman physically, contacting her repeatedly against her will, or spying/monitoring her online activities (cyberstalking). First conviction is bailable, subsequent ones are non-bailable.",
        "BNS Section 78, Stalking, Cyberstalking, Monitoring Online, IPC 354D",
        "State of Maharashtra v. Robin", 2017,
        "Established that digital messages, continuous calling, and tracking a woman online constitute a violation of privacy and amount to stalking.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Medium", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Bailable for first conviction (Non-bailable for subsequent)",
        "Imprisonment up to 3 years and fine for first offense; up to 5 years and fine for second offense.",
        "Exceptions: Stalking for the purpose of preventing or detecting crime under state authorization.", "Information Technology Act 2000",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-009", "Statute", "Chapter V - Offences Against Woman and Child", "Section 80", "Dowry Death under BNS",
        "Where the death of a woman is caused by any burns or bodily injury or occurs otherwise than under normal circumstances within seven years of her marriage, and it is shown that soon before her death she was subjected to cruelty or harassment by her husband or any relative of her husband for, or in connection with, any demand for dowry, such death shall be called dowry death.",
        "Section 80 of BNS (formerly Section 304B of IPC) defines dowry death. If a woman dies in abnormal circumstances within 7 years of marriage and it is proved that she was harassed for dowry soon before her death, the husband or relative is presumed to have caused her death. Minimum punishment is 7 years.",
        "BNS Section 80, Dowry Death, S.80 BNS, Harassment, Cruelty, Demand for Dowry, IPC 304B",
        "Sher Singh v. State of Haryana", 2015,
        "The phrase 'soon before' does not mean 'immediately before'. There must be a proximate and live link between the dowry harassment and the death.",
        "Shanti v. State of Haryana", 1991, "Established the three essential ingredients: abnormal death within 7 years, harassment soon before death, and harassment related to dowry demand.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Imprisonment of not less than 7 years, which may extend to life imprisonment.",
        "Must occur within 7 years of marriage.", "Section 85 BNS, Indian Evidence Act S.113B (now BSA S.116)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-010", "Statute", "Chapter V - Offences Against Woman and Child", "Section 85", "Cruelty by Husband or Relatives",
        "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "Section 85 of BNS (formerly Section 498A of IPC) subjects cruelty by husband or his relatives. Cruelty includes physical/mental harassment which drives the woman to suicide or harassment to coerce her/family to meet illegal property or dowry demands.",
        "BNS Section 85, Cruelty, Mental Harassment, Dowry demand, S.85 BNS, IPC 498A",
        "Arnesh Kumar v. State of Bihar", 2014,
        "Directed that police should not automatically arrest the husband and relatives under S.498A IPC without complying with CrPC Section 41A parameters to prevent misuse.",
        "Sushil Kumar Sharma v. Union of India", 2005, "Upheld the constitutionality of Section 498A but acknowledged that it is sometimes used as a shield rather than a weapon, calling on courts to prevent abuse.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Imprisonment up to 3 years and fine.",
        "Filing of false complaints can be treated as mental cruelty in divorce proceedings.", "Section 80 BNS, Protection of Women from Domestic Violence Act 2005",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-011", "Statute", "Chapter VI - Offences Affecting the Human Body", "Section 101", "Murder defined in BNS",
        "Except in the cases hereinafter excepted, culpable homicide is murder, if the act by which the death is caused is done with the intention of causing death, or causing such bodily injury as the offender knows is likely to cause death, or is sufficient in the ordinary course of nature to cause death.",
        "Section 101 of BNS (formerly Section 300 of IPC) defines Murder. It is culpable homicide committed with: 1. Intention to cause death; 2. Intention to cause bodily injury sufficient to cause death; 3. Knowledge that the act is so imminently dangerous that it must cause death. It has 5 exceptions (grave/sudden provocation, private defense, public servant acting in good faith, sudden fight, consent).",
        "BNS Section 101, Murder, S.101 BNS, Intention, Bodily Injury, IPC 300, IPC 302",
        "K.M. Nanavati v. State of Maharashtra", 1962,
        "Laid down the test for grave and sudden provocation; the provocation must be such as to deprive a reasonable man of self-control.",
        "State of Andhra Pradesh v. Rayavarapu Punnayya", 1976, "Distinguished between culpable homicide (genus) and murder (species) based on degrees of probability of death.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Punished under Section 103 BNS.",
        "Subject to the five exceptions specified in Section 101 BNS.", "Section 100 BNS, Section 103 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-012", "Statute", "Chapter VI - Offences Affecting the Human Body", "Section 103", "Punishment for Murder and Mob Lynching",
        "Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine. Where a group of five or more persons commits murder on the ground of race, caste, community, sex, place of birth, language, personal belief or any other similar ground, each member of such group shall be punished with death or life imprisonment.",
        "Section 103 of BNS (replaces Section 302 of IPC) provides the punishment for murder: death or life imprisonment, and a fine. Critically, Section 103(2) introduces a new provision for Mob Lynching: where a group of 5 or more persons commits murder based on race, caste, community, sex, language, etc., they face death or life imprisonment.",
        "BNS Section 103, S.103 BNS, Punishment for Murder, Mob Lynching, Caste Violence, IPC 302",
        "Bachan Singh v. State of Punjab", 1980,
        "Established the 'rarest of rare cases' doctrine for awarding the death penalty; aggravating and mitigating circumstances must be balanced.",
        "Machhi Singh v. State of Punjab", 1983, "Guidelines for applying the rarest of rare cases doctrine, listing factors like manner of commission, motive, and anti-social nature of the crime.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Death penalty or imprisonment for life, and fine.",
        "Subject to the judicial interpretation of the rarest of rare doctrine for capital punishment.", "Section 101 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-013", "Statute", "Chapter VI - Offences Affecting the Human Body", "Section 109", "Attempt to Murder in BNS",
        "Whoever does any act with such intention or knowledge, and under such circumstances that, if he by that act caused death, he would be guilty of murder, shall be punished.",
        "Section 109 of BNS (formerly Section 307 of IPC) punishes Attempt to Murder. If a person does an act with the intention/knowledge that it would cause murder if successful, they can be imprisoned up to 10 years and fined. If hurt is caused to any person by the act, the punishment can extend to life imprisonment.",
        "BNS Section 109, Attempt to Murder, S.109 BNS, Hurt caused, IPC 307",
        "State of Maharashtra v. Balram Bama Patil", 1983,
        "To establish S.307 IPC, it is not necessary that bodily injury capable of causing death should have been inflicted; what matters is the intention/knowledge and the act towards it.",
        "State of Madhya Pradesh v. Kanha", 2019, "Reaffirmed that the nature of injury is not sole criteria; intention can be gathered from the nature of weapon, parts targeted, and circumstances.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Imprisonment up to 10 years and fine; if hurt is caused, extends to life imprisonment.",
        "The act must be an attempt; mere preparation is not enough.", "Section 101 BNS, Section 103 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-014", "Statute", "Chapter VI - Offences Affecting the Human Body", "Section 111", "Organised Crime in BNS",
        "Any continuing unlawful activity including kidnapping, robbery, dacoity, extortion, land grabbing, contract killing, cyber crimes, running human trafficking, economic offences, committed by a syndicate or organized gang is organized crime.",
        "Section 111 of BNS is a NEW provision that criminalizes Organised Crime. It covers illegal activities like kidnapping, extortion, dacoity, land grabbing, contract killing, cybercrime, or trafficking done by a gang or criminal syndicate. If death is caused, punishment is death or life imprisonment. Otherwise, minimum 5 years.",
        "BNS Section 111, S.111 BNS, Organised Crime, Crime Syndicate, Extortion, Contract Killing, Cybercrime, MCOCA Equivalent",
        "State of Maharashtra v. Lalit Somdatta Nagpal", 2007,
        "Decided under MCOCA (Maharashtra Control of Organised Crime Act) establishing strict standards for proving organized crime syndicates.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "If death is caused: death or life imprisonment, and a minimum fine of 10 lakh rupees. Otherwise: 5 years to life imprisonment, and minimum fine of 5 lakh rupees.",
        "Requires proof of continuing unlawful activity and syndicate association.", "Section 112 BNS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-015", "Statute", "Chapter VI - Offences Affecting the Human Body", "Section 124", "Acid Attack under BNS",
        "Whoever causes permanent or partial damage or deformity, or burns or maims or disfigures or disables, any part or parts of the body of a person or causes grievous hurt by throwing acid or by administering acid, shall be punished.",
        "Section 124 of BNS (replaces Section 326A of IPC) criminalizes acid attacks. It punishes throwing or administering acid causing permanent or partial deformity, disability, or burns. The minimum punishment is 10 years of rigorous imprisonment, which may extend to life, and the fine must go directly to the victim to cover medical expenses.",
        "BNS Section 124, Acid Attack, Throwing Acid, Grievous Hurt by Acid, IPC 326A, IPC 326B",
        "Laxmi v. Union of India", 2014,
        "Supreme Court regulated the retail sale of acid, directed compensation for acid attack survivors, and mandated free medical treatment.",
        "State of Himachal Pradesh v. Sandeep Kumar", 2017, "Emphasized that no leniency should be shown in sentencing acid attackers due to the permanent physical and psychological trauma to the victim.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Rigorous imprisonment of not less than 10 years, extending to life, and fine (payable to the victim for medical treatment).",
        "The fine must be reasonable to meet medical expenses.", "Section 124(2) BNS (Attempt - old 326B)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-016", "Statute", "Chapter VII - Offences Against State", "Section 152", "Acts Endangering Sovereignty, Unity and Integrity of India",
        "Whoever, purposely or knowingly, by words, either spoken or written, or by signs, or by visible representation, or by electronic communication or by use of financial means, excites or attempts to excite, secession or armed rebellion or subversive activities, shall be punished.",
        "Section 152 of BNS replaces the controversial 'Sedition' law (formerly Section 124A of IPC). It criminalizes acts that excite secession, armed rebellion, or subversive activities, or endanger the sovereignty, unity, and integrity of India, using speech, writing, electronic means, or funding. Sedition is technically removed, but the scope of crimes against the state is modernized to include digital and financial means.",
        "BNS Section 152, S.152 BNS, Sedition Replaced, Sovereignty of India, Secession, Subversive Activities, IPC 124A",
        "Kedar Nath Singh v. State of Bihar", 1962,
        "Sedition (124A) is constitutional but only applies when there is incitement to violence or public disorder; strong criticism of govt is not seditious.",
        "S.G. Vombatkere v. Union of India", 2022, "Supreme Court kept Section 124A IPC in abeyance, directing governments to refrain from registering FIRs under it pending legislative review, which led to Section 152 BNS.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable",
        "Imprisonment for life or rigorous imprisonment up to 7 years, and fine.",
        "Criticism of government policies without inciting violence or secession does not fall under S.152.", "Unlawful Activities (Prevention) Act 1967",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-017", "Statute", "Chapter XVII - Offences Against Property", "Section 303", "Theft under BNS",
        "Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.",
        "Section 303 of BNS (formerly Section 378 and 379 of IPC) defines and punishes theft. It involves dishonestly taking movable property out of a person's possession without their consent, and moving it for that purpose. Punishable with up to 3 years of imprisonment, or fine, or both. For a second conviction, community service can be ordered.",
        "BNS Section 303, S.303 BNS, Theft, Movable Property, Dishonest Intention, IPC 378, IPC 379",
        "Pyare Lal Bhargava v. State of Rajasthan", 1963,
        "To constitute theft, temporary deprivation of property is sufficient; permanent taking is not required.",
        "K.N. Mehra v. State of Rajasthan", 1957, "Taking out an aircraft without permission for a joyride constitutes theft as it causes wrongful loss to the owner.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Bailable (except specific sub-sections or repeat offenses)",
        "Imprisonment up to 3 years, or fine, or both; community service for repeat offenders.",
        "Must be movable property in someone's possession.", "Section 305 BNS (Theft in house - old 380)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-018", "Statute", "Chapter XVII - Offences Against Property", "Section 318", "Cheating under BNS",
        "Whoever, by deceiving any person, fraudulently or dishonestly induces the person so deceived to deliver any property to any person, or to consent that any person shall retain any property, commits cheating.",
        "Section 318 of BNS (formerly Sections 415 and 420 of IPC) governs cheating. It involves deceiving a person to deliver property or make them do something they wouldn't do otherwise. Punishment under Section 318(4) (formerly S.420 IPC) for cheating and dishonestly inducing delivery of property is up to 7 years of imprisonment and fine.",
        "BNS Section 318, Cheating, Delivery of Property, Fraudulent inducement, IPC 415, IPC 420, S.318 BNS",
        "State of Kerala v. A. Pareed Pillai", 1973,
        "To hold a person guilty of cheating, fraudulent or dishonest intention must be shown to exist at the time of making the promise.",
        "Sushil Sethi v. State of Arunachal Pradesh", 2020, "For cheating, there must be a dishonest intention from the very beginning; mere breach of contract is not cheating.",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Cognizable / Non-bailable (for serious subsets like delivery of property)",
        "Imprisonment up to 3 years (general); up to 7 years and fine under S.318(4) for delivery of property.",
        "Distinction between breach of contract and cheating depends on the presence of dishonest intention at inception.", "Section 316 BNS (Breach of trust)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ],
    [
        "BNS-019", "Statute", "Chapter XIX - Defamation, Criminal Intimidation, Insult etc.", "Section 356", "Defamation under BNS",
        "Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said to defame.",
        "Section 356 of BNS (formerly Section 499 and 500 of IPC) defines and punishes defamation. It protects personal reputation from false imputations. Punishable by up to 2 years of imprisonment, or fine, or both, or community service. It retains the same 10 exceptions (truth for public good, public conduct of public servants, etc.).",
        "BNS Section 356, Defamation, Libel, Slander, Community Service, IPC 499, IPC 500, S.356 BNS",
        "Subramanian Swamy v. Union of India", 2016,
        "Upheld the constitutionality of criminal defamation (Sections 499/500 IPC); right to reputation is part of Article 21.",
        "Shreya Singhal v. Union of India", 2015, "Decided on online speech and boundaries of offensive content vs defamation under Article 19(1)(a).",
        "High", "Criminal Law - BNS", 2024, "Ministry of Home Affairs",
        "Non-cognizable / Bailable",
        "Simple imprisonment up to 2 years, or fine, or both, or community service.",
        "Subject to 10 exceptions like true statement for public good, expression of opinion in good faith.", "Civil Defamation (Tort law)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nyaya Sanhita (BNS)", "Active"
    ]
]

bnss_rows = [
    [
        "BNSS-001", "Statute", "Chapter XII - Information to the Police and Powers to Investigate", "Section 173", "First Information Report (FIR), Zero FIR and e-FIR",
        "Every information relating to the commission of a cognizable offence, if given orally to an officer in charge of a police station, shall be reduced to writing. Information may be given by electronic communication.",
        "Section 173 of BNSS (replaces Section 154 of CrPC) details FIR procedures. It formally codifies: 1. Zero FIR (an FIR can be filed at any police station regardless of jurisdiction); 2. e-FIR (information can be sent digitally, and the informant must sign it within 3 days). It also introduces a preliminary inquiry before registering FIRs for offenses punishable with 3 to 7 years.",
        "BNSS Section 173, FIR, Zero FIR, e-FIR, Digital Signature, Preliminary Inquiry, CrPC 154",
        "Lalita Kumari v. Govt. of Uttar Pradesh", 2014,
        "Registration of FIR is mandatory under Section 154 of CrPC if the information discloses commission of a cognizable offence; no preliminary inquiry is permitted except in specific cases (like medical negligence, matrimonial disputes).",
        "State of Andhra Pradesh v. Punati Ramulu", 1993, "Police cannot refuse to record information about a cognizable offence on the ground of lack of territorial jurisdiction; they must register it (Zero FIR concept).",
        "High", "Criminal Procedure - BNSS", 2024, "Ministry of Home Affairs",
        "Procedural Law", "Not Applicable / N.A.",
        "Preliminary inquiry allowed for offenses with 3-7 years punishment before registering FIR, to be completed in 14 days.",
        "Section 176 BNSS", "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nagarik Suraksha Sanhita (BNSS)", "Active"
    ],
    [
        "BNSS-002", "Statute", "Chapter V - Arrest of Persons", "Section 35", "summons and Arrest procedures under BNSS",
        "Any police officer may without an order from a Magistrate and without a warrant, arrest any person who commits a cognizable offence in his presence, or against whom a reasonable complaint has been made.",
        "Section 35 of BNSS (replaces Section 41 of CrPC) defines when police can arrest without a warrant. It requires the police officer to satisfy themselves that the arrest is necessary to prevent further offense, tampering, or disappearing of evidence. For offenses punishable by less than 7 years, arrest is not mandatory unless specific conditions are met, and S.35(3) mandates issuing a notice of appearance first.",
        "BNSS Section 35, S.35 BNSS, Arrest without warrant, Notice of Appearance, CrPC 41, CrPC 41A",
        "D.K. Basu v. State of West Bengal", 1997,
        "Laid down mandatory guidelines to be followed by police during arrest and detention to prevent custodial violence.",
        "Arnesh Kumar v. State of Bihar", 2014, "Arrest should be the exception, not the rule, in offenses carrying less than 7 years of imprisonment; S.41A notice of appearance must be issued first.",
        "High", "Criminal Procedure - BNSS", 2024, "Ministry of Home Affairs",
        "Procedural Law", "Not Applicable / N.A.",
        "Arrests for minor offenses are subject to guidelines under S.35(1) and S.35(3) BNSS.", "Section 37 BNSS (Designated arrest officer)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nagarik Suraksha Sanhita (BNSS)", "Active"
    ],
    [
        "BNSS-003", "Statute", "Chapter XV - Documents and Custody", "Section 187", "Police Custody and Detention Timelines",
        "The Magistrate may authorize the detention of the accused in such custody as such Magistrate thinks fit, for a term not exceeding fifteen days in the whole or in parts during the initial forty days or sixty days.",
        "Section 187 of BNSS replaces Section 167 of CrPC. It makes a major change: police custody of 15 days no longer needs to be continuous. It can be granted in parts throughout the first 40 or 60 days of the 60/90-day investigation window. Total detention (judicial + police custody) remains capped at 60 or 90 days before default bail kicks in.",
        "BNSS Section 187, S.187 BNSS, Police Custody, Default Bail, Judicial Custody, CrPC 167",
        "CBI v. Anupam J. Kulkarni", 1992,
        "Under the old CrPC, police custody was allowed only during the first 15 days of remand; this limit has been modified by BNSS Section 187.",
        "Sanjay Dutt v. State", 1994, "Indicated that the right to default bail is absolute if the charge sheet is not filed within the statutory period.",
        "High", "Criminal Procedure - BNSS", 2024, "Ministry of Home Affairs",
        "Procedural Law", "Not Applicable / N.A.",
        "Custody can only be granted in parts during initial 40 or 60 days of the remand period.", "Section 480 BNSS (Bail)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nagarik Suraksha Sanhita (BNSS)", "Active"
    ],
    [
        "BNSS-004", "Statute", "Chapter VII - Summons to Produce Things and Search", "Section 185", "Mandatory Videography of Search and Seizure",
        "The police officer conducting a search shall prepare a list of all things seized. The process of search and seizure shall be recorded through audio-video electronic means.",
        "Section 185 of BNSS introduces a critical safeguard: the entire process of search and seizure by police must be video-recorded (e.g., on a mobile phone or video camera). The recording, along with the list of seized items, must be forwarded to the Magistrate without delay to prevent police planting of evidence.",
        "BNSS Section 185, Search and Seizure, Videography, Audio-video recording, S.185 BNSS, Search List",
        "Shafhi Mohammad v. State of Himachal Pradesh", 2018,
        "Recognized the utility of videography in crime scene investigations and search operations to ensure transparency and prevent false allegations.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Criminal Procedure - BNSS", 2024, "Ministry of Home Affairs",
        "Procedural Law", "Not Applicable / N.A.",
        "Recording must be done without delay and submitted to the magistrate.", "BSA Section 63 (electronic evidence admissibility)",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nagarik Suraksha Sanhita (BNSS)", "Active"
    ],
    [
        "BNSS-005", "Statute", "Chapter XXXV - Bail and Bonds", "Section 479", "Bail for First-Time Offenders and Undertrials",
        "Where a person has, during the period of investigation or trial under this Sanhita, undergone detention for a period extending up to one-half of the maximum period of imprisonment, he shall be released by the Court on bail.",
        "Section 479 of BNSS (replaces Section 436A of CrPC) provides relief for undertrials. A person who has spent half of the maximum prison sentence of the alleged offense in jail must be released on bail. Crucially, a first-time offender (who has never been convicted of any offense before) must be released on bail after spending one-third of the maximum sentence in jail.",
        "BNSS Section 479, Undertrial Bail, First-time Offender, S.479 BNSS, CrPC 436A",
        "Bhim Singh v. Union of India", 2014,
        "Supreme Court directed jurisdictional magistrates and judges to identify undertrials who completed half of their maximum sentences and order their release on bail.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Criminal Procedure - BNSS", 2024, "Ministry of Home Affairs",
        "Procedural Law", "Bail is a right for bailable offenses, and conditional for non-bailable.",
        "Does not apply to offenses punishable with death or life imprisonment, or where trial is delayed due to accused actions.", "Section 480 BNSS, Section 482 BNSS",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Nagarik Suraksha Sanhita (BNSS)", "Active"
    ]
]

bsa_rows = [
    [
        "BSA-001", "Statute", "Chapter V - Of Documentary Evidence", "Section 63", "Admissibility of Electronic and Digital Records",
        "Any information contained in an electronic record which is printed on a paper, stored, recorded or copied in optical or magnetic media shall be deemed to be also a document and shall be admissible in any proceedings.",
        "Section 63 of BSA (replaces Section 65B of IPC/IEA) governs electronic evidence (emails, WhatsApp messages, digital logs, photos). It simplifies the admissibility process. A signed certificate by a person in charge of the device or an expert is still required, but the law expands the definition of electronic records to include cloud storage and digital signatures.",
        "BSA Section 63, Electronic Evidence, WhatsApp chats, Certificate S.63, Digital Records, IEA 65B",
        "Anvar P.V. v. P.K. Basheer", 2014,
        "Under the old IEA, a written certificate under S.65B(4) was mandatory to admit secondary electronic records; oral evidence cannot substitute it.",
        "Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal", 2020, "Reaffirmed that the Section 65B certificate is a condition precedent to the admissibility of secondary electronic evidence.",
        "High", "Law of Evidence - BSA", 2024, "Ministry of Law and Justice",
        "Admissibility criteria", "Not Applicable / N.A.",
        "Requires a certificate verifying the authenticity and device conditions during record generation.", "Section 61 BSA, Section 62 BSA",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Sakshya Adhiniyam (BSA)", "Active"
    ],
    [
        "BSA-002", "Statute", "Chapter II - Relevancy of Facts", "Section 23", "Dying Declaration under BSA",
        "Statements, written or verbal, of relevant facts made by a person who is dead, or who cannot be found, are themselves relevant facts when the statement is made by a person as to the cause of his death.",
        "Section 23 of BSA (formerly Section 32(1) of the Indian Evidence Act) makes a dying declaration admissible. If a person makes a statement about the cause of their death or the transactions leading to it, it is highly relevant. If it is voluntary and truthful, the court can convict based solely on it.",
        "BSA Section 23, S.23 BSA, Dying Declaration, Cause of Death, Hearsay Exception, IEA 32",
        "Pakala Narayana Swami v. Emperor", 1939,
        "Established that statements made by a person before death about the circumstances of transactions that resulted in their death are admissible.",
        "Khushal Rao v. State of Bombay", 1958, "Laid down the principles governing dying declarations: it can form the sole basis of conviction if found reliable and untutored.",
        "High", "Law of Evidence - BSA", 2024, "Ministry of Law and Justice",
        "Relevancy of statements", "Not Applicable / N.A.",
        "Must be made when the person is in a fit state of mind; doctor's certificate is preferred but not mandatory.", "Section 24 BSA",
        "Legislative Enactment", "In force", "https://www.indiacode.nic.in/", "Bharatiya Sakshya Adhiniyam (BSA)", "Active"
    ]
]

it_rows = [
    # IT-001 New Regime Slabs
    [
        "IT-001", "Statute", "Chapter XII - Determination of Tax in Certain Special Cases", "Section 115BAC", "New Tax Regime Slabs (AY 2024-25 and FY 2025-26)",
        "The income-tax payable in respect of the total income of a person, being an individual or HUF, shall, at his option or by default, be computed at concessional rates.",
        "Section 115BAC details the New Tax Regime, which is the default regime from AY 2024-25. Slabs for FY 2025-26 (AY 2026-27): Up to ₹4,00,000: Nil; ₹4,00,001 to ₹8,00,000: 5%; ₹8,00,001 to ₹12,00,000: 10%; ₹12,00,001 to ₹16,00,000: 15%; ₹16,00,001 to ₹20,00,000: 20%; ₹20,00,001 to ₹24,00,000: 25%; Above ₹24,00,000: 30%. Standard deduction is ₹75,000. Rebate S.87A makes tax nil up to ₹7 Lakhs (plus standard deduction). Most deductions (80C, 80D, S.24) are not allowed under this regime.",
        "Income Tax Slabs, New Tax Regime, Section 115BAC, Standard Deduction, Tax Slabs 2025, S.115BAC",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2020, "Ministry of Finance - CBDT",
        "Tax Rates / Slabs", "Not Applicable / N.A.",
        "Taxpayer must opt-out to choose the old regime.", "Section 80C, Section 87A",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-002 Old Regime Slabs
    [
        "IT-002", "Statute", "Chapter I - Charge of Income-tax", "Section 4 (Old Regime Slabs)", "Old Tax Regime Slabs and Rates",
        "Income-tax shall be charged at the rates specified in the Finance Act in respect of the total income of the previous year of every person.",
        "The Old Tax Regime slabs (which allow all standard exemptions and deductions): Up to ₹2,50,000: Nil; ₹2,50,001 to ₹5,00,000: 5% (fully rebated under S.87A up to 5L); ₹5,00,001 to ₹10,00,000: 20%; Above ₹10,00,000: 30%. Taxpayers can avail deductions under Section 80C (PPF, LIC, etc.), Section 80D (health insurance), Section 24(b) (home loan interest), and HRA exemption.",
        "Old Tax Regime Slabs, Old Tax slabs, Section 80C deductions, HRA exemption slabs, old vs new regime",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Tax Rates / Slabs", "Not Applicable / N.A.",
        "Taxpayers must actively opt into the Old Regime during filing; otherwise New Regime applies by default.", "Section 115BAC, Section 80C",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-003 Section 80C
    [
        "IT-003", "Statute", "Chapter VI-A - Deductions in Respect of Certain Incomes", "Section 80C", "Section 80C Deductions (1.5 Lakh Limit)",
        "In computing the total income of an assessee, there shall be deducted, in accordance with and subject to the provisions of this section, any sums paid or deposited in the previous year by the assessee.",
        "Section 80C provides a tax deduction of up to ₹1,50,000 per year from gross total income. Allowed investments: Public Provident Fund (PPF), Employee Provident Fund (EPF), Equity Linked Savings Schemes (ELSS), Life Insurance Premium, National Savings Certificate (NSC), Principal repayment of Home Loan, Tuition Fees for up to 2 children, Sukanya Samriddhi Yojana (SSY), and 5-year tax-saving fixed deposits. Only available in the Old Tax Regime.",
        "Section 80C, PPF, ELSS, Tax Saving, Life Insurance, Home Loan Principal, S.80C, Deductions",
        "CIT v. Rajasthan State Electricity Board", 1997,
        "Deduction is allowable on actual payment basis during the relevant financial year.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Deductions from Income", "Maximum ₹1,50,000 per financial year",
        "Not available to taxpayers under the New Tax Regime S.115BAC.", "Section 80CCC, Section 80CCD",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-004 Section 80D
    [
        "IT-004", "Statute", "Chapter VI-A - Deductions in Respect of Certain Incomes", "Section 80D", "Medical Insurance Premium Deduction",
        "In computing the total income of an assessee, there shall be deducted sums paid to effect or keep in force an insurance on the health of the assessee or his family or parents.",
        "Section 80D allows a deduction for health insurance premium and preventive health check-up. 1. Self, Spouse, and Dependent Children: Limit is ₹25,000 (increases to ₹50,000 if self/spouse is a senior citizen). 2. Parents: Additional limit of ₹25,000 (increases to ₹50,000 if parent is a senior citizen). Max deduction can be ₹1,00,000 (both self and parents are senior citizens). Preventive health check-up is capped at ₹5,000 (within the overall limit). Payment must be made by any mode other than cash (cash is allowed only for preventive health check-ups). Only available in the Old Tax Regime.",
        "Section 80D, Health Insurance, Medical Claim, Senior Citizen health, S.80D, Deductions",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Deductions from Income", "Up to ₹25,000 / ₹50,000 / ₹1,00,000 depending on senior citizen status",
        "Insurance premium payments must not be made in cash; cash is permitted only for preventive health check-ups up to ₹5,000.", "Section 80C",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-005 Home loan interest S.24
    [
        "IT-005", "Statute", "Chapter IV - Computation of Total Income", "Section 24(b)", "Deduction for Home Loan Interest",
        "Where the property has been acquired, constructed, repaired, renewed or reconstructed with borrowed capital, the amount of any interest payable on such capital shall be deducted.",
        "Section 24(b) allows deduction of interest paid on a home loan. For a self-occupied property, the maximum deduction is ₹2,00,000 per financial year. Construction or purchase must be completed within 5 years from the end of the FY in which capital was borrowed; otherwise, the limit is reduced to ₹30,000. For let-out properties, there is no limit on interest deduction, but loss from house property that can be offset against other income is capped at ₹2,00,000. Only available in the Old Tax Regime.",
        "Section 24, Home Loan Interest, Loss from House Property, Self-occupied property interest, S.24(b)",
        "CIT v. Podar Cement Pvt. Ltd.", 1997,
        "Established that for tax purposes, the owner of a house property is the person who receives the income, even if registration formalities are incomplete.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Income from House Property", "Maximum ₹2,00,000 for self-occupied property",
        "Reduced to ₹30,000 if construction is not completed within 5 years from loan year.", "Section 80C (Principal repayment)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-006 Presumptive business S.44AD
    [
        "IT-006", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 44AD", "Presumptive Taxation for Businesses",
        "Notwithstanding anything to the contrary contained in sections 28 to 43C, in the case of an eligible assessee engaged in an eligible business, a sum equal to eight per cent of the total turnover or gross receipts shall be deemed to be the profits.",
        "Section 44AD offers a simplified presumptive tax scheme for small businesses. Income is estimated at 8% of total turnover/gross receipts (reduced to 6% for receipts via digital transactions like UPI, net banking, cards). The turnover limit to opt for this scheme is ₹3 Crore (if cash transactions are under 5% of gross receipts; otherwise ₹2 Crore). Taxpayers under this scheme do not need to maintain detailed books of accounts or get an audit.",
        "Section 44AD, Presumptive Taxation, Small Business, Books of Accounts Audit, S.44AD, 6 percent, 8 percent",
        "CIT v. Reliance Petroproducts Pvt. Ltd.", 2010,
        "Determined that making a claim that is not accepted by the Assessing Officer does not automatically attract penalty under S.271(1)(c) for inaccurate particulars.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Profits and Gains of Business or Profession", "6% on digital turnover and 8% on cash turnover",
        "Only available to resident individuals, HUFs, and partnership firms (excluding LLP).", "Section 44ADA (Professionals), Section 44AB (Audit)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-007 Presumptive professional S.44ADA
    [
        "IT-007", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 44ADA", "Presumptive Taxation for Professionals",
        "In the case of an assessee, being a resident in India, who is engaged in a profession referred to in sub-section (1) of section 44AA, a sum equal to fifty per cent of the total gross receipts shall be deemed to be the profits.",
        "Section 44ADA offers a presumptive tax scheme for professionals (doctors, engineers, CAs, lawyers, architects, IT professionals). The gross receipts limit is ₹75 Lakhs (if cash receipts are under 5% of total; otherwise ₹50 Lakhs). Profits are presumed to be 50% of gross receipts, and the professional pays tax on this amount. No need to maintain books of accounts or undergo tax audit.",
        "Section 44ADA, Presumptive Professional, Doctors Engineers Lawyers CAs tax, S.44ADA",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2016, "Ministry of Finance - CBDT",
        "Profits and Gains of Business or Profession", "50% of gross receipts deemed as taxable income",
        "Only applicable to specific professions listed under Section 44AA(1).", "Section 44AD, Section 44AB",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-008 LTCG Equity S.112A
    [
        "IT-008", "Statute", "Chapter XII - Determination of Tax in Certain Special Cases", "Section 112A", "LTCG Tax on Equity and Mutual Funds",
        "The tax payable by an assessee on long-term capital gains exceeding one lakh twenty-five thousand rupees from transfer of equity shares, equity oriented mutual funds, or business trust units shall be calculated at twelve and a half per cent.",
        "Section 112A governs Long-Term Capital Gains (LTCG) tax on equity shares and equity-oriented mutual funds (held for more than 12 months). Effective from July 2024, gains exceeding ₹1.25 Lakhs in a financial year are taxed at 12.5% (previously 10% above ₹1 Lakh). No indexation benefit is allowed for these assets under S.112A.",
        "Section 112A, LTCG, Long Term Capital Gains, Shares Mutual Funds, 12.5 percent, S.112A",
        "CIT v. Vodafone International Holdings BV", 2012,
        "A landmark judgment on taxation of capital gains in offshore transactions, establishing boundaries of tax planning vs tax evasion.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2018, "Ministry of Finance - CBDT",
        "Capital Gains Tax", "12.5% on gains exceeding ₹1.25 Lakhs",
        "STT (Securities Transaction Tax) must have been paid on purchase and sale of shares.", "Section 111A (STCG), Section 112",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-009 STCG Equity S.111A
    [
        "IT-009", "Statute", "Chapter XII - Determination of Tax in Certain Special Cases", "Section 111A", "STCG Tax on Equity and Mutual Funds",
        "The tax payable by an assessee on short-term capital gains from transfer of equity shares, equity oriented mutual funds, or business trust units shall be calculated at twenty per cent.",
        "Section 111A governs Short-Term Capital Gains (STCG) tax on equity shares and equity-oriented mutual funds (held for 12 months or less). Effective from July 2024, these gains are taxed at 20% (previously 15%). The transaction must be subject to Securities Transaction Tax (STT).",
        "Section 111A, STCG, Short Term Capital Gains, Shares Mutual Funds, 20 percent, S.111A",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2004, "Ministry of Finance - CBDT",
        "Capital Gains Tax", "20% flat rate",
        "STT must have been paid at the time of sale.", "Section 112A (LTCG)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-010 HRA Exemption S.10(13A)
    [
        "IT-010", "Statute", "Chapter II - Incomes which do not form part of Total Income", "Section 10(13A)", "House Rent Allowance (HRA) Exemption",
        "Any special allowance specifically granted to an assessee by his employer to meet expenditure actually incurred on payment of rent in respect of residential accommodation occupied by him is exempt.",
        "Section 10(13A) governs the tax exemption on House Rent Allowance (HRA) for salaried employees. The exempt amount is the minimum of three values: 1. Actual HRA received; 2. Rent paid minus 10% of basic salary; 3. 50% of basic salary (for metro cities: Delhi, Mumbai, Kolkata, Chennai) or 40% of basic salary (for non-metro cities). Taxpayer must live in rented accommodation and pay rent. Only available under the Old Tax Regime.",
        "Section 10(13A), HRA Exemption, House Rent Allowance, Rent receipts, HRA Calculator, S.10(13A)",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Exemptions under Salary", "Minimum of the three specified conditions",
        "Not available to taxpayers under the New Tax Regime S.115BAC.", "Section 80GG (Rent deduction when HRA not received)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-011 S.37(1) General business deduction
    [
        "IT-011", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 37(1)", "General Business Expenses Deduction",
        "Any expenditure (not being expenditure of the character described in sections 30 to 36 and not being in the nature of capital expenditure or personal expenses of the assessee), laid out or expended wholly and exclusively for the purposes of the business or profession shall be allowed.",
        "Section 37(1) is the general section that allows deduction of any business expense not covered under other specific sections (S.30-36). The expense must be: 1. Revenue in nature (not capital); 2. Wholly and exclusively for the business; 3. Not personal in nature; 4. Not for any purpose that is an offense or prohibited by law. Common examples include salary to staff, office rent, electricity, printing, advertising, traveling, and communication costs.",
        "Section 37, Business expenses deduction, office rent utility, salary to staff tax deduction, revenue expenditure, S.37(1)",
        "CIT v. Malayalam Plantations Ltd.", 1964,
        "The expression 'for the purpose of the business' is wider than 'for the purpose of earning profits'. It covers administration, preservation, and protection of business.",
        "CIT v. Reliance Petroproducts Pvt. Ltd.", 2010, "Simply making an incorrect claim of deduction under S.37 does not amount to providing inaccurate particulars or attract concealment penalty.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Business Deduction", "Allowed fully if expenses are genuine and exclusively for business",
        "Expenditure incurred on CSR (Corporate Social Responsibility) is not allowed as business expenditure under S.37(1).", "Section 30 to 36",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-012 S.40A(3) Cash payments limit
    [
        "IT-012", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 40A(3)", "Disallowance of Cash Payments above 10,000",
        "Where the assessee incurs any expenditure in respect of which a payment or aggregate of payments made to a person in a day, otherwise than by an account payee cheque or account payee bank draft or electronic clearing system, exceeds ten thousand rupees, no deduction shall be allowed.",
        "Section 40A(3) disallows tax deductions for business expenses if the payment is made in cash and exceeds ₹10,000 to a single person in a single day. The entire expense is disallowed and added back to taxable profits. For payments made to transport operators (hiring/leasing goods carriages), the cash limit is higher, at ₹35,000.",
        "Section 40A(3), Cash payment disallowance, cash limit 10000, transporter cash limit 35000, business cash payments, S.40A(3)",
        "Attar Singh Gurmukh Singh v. CIT", 1991,
        "Supreme Court upheld the validity of S.40A(3); it is designed to check tax evasion, ensure cash flow transparency, and verify transaction genuineness.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Business Disallowance", "100% of the expenditure is disallowed if paid in cash above ₹10,000",
        "Exceptions listed under Rule 6DD (e.g. payments to RBI, banks, government, cultivators for agricultural produce, or where banking facilities are unavailable).", "Rule 6DD",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-013 S.43B and MSME payment rule
    [
        "IT-013", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 43B", "Deductions Allowed only on Actual Payment (including MSME S.43B(h))",
        "Notwithstanding anything contained in any other provision of this Act, a deduction otherwise allowable under this Act in respect of any sum payable... shall be allowed only in computing the income of the previous year in which such sum is actually paid.",
        "Section 43B lists expenses that are allowed as deductions only in the financial year they are actually paid, rather than when they are accrued. This includes taxes, duties, provident fund/ESI contributions, interest on bank loans, and leave encashment. Crucially, Section 43B(h) (introduced from FY 2023-24) mandates that payments to registered Micro and Small Enterprises (MSMEs) must be made within the time limit specified in the MSMED Act, 2006 (within 15 days, or max 45 days if there is a written agreement). If not paid within this limit, the deduction is disallowed in that FY and allowed only in the year of payment.",
        "Section 43B, Actual payment deduction, MSME 45 days payment rule, Section 43B(h) MSME, delayed payment to small business, disallowance",
        "Allied Motors Pvt. Ltd. v. CIT", 1997,
        "Established that if sales tax/duty is paid before the due date of filing the income tax return, the deduction under S.43B is allowed in the year of accrual.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Business Deduction on Cash Basis", "Disallowed if unpaid within due dates",
        "S.43B(h) does not apply to Medium enterprises (only Micro and Small) and does not apply to traders.", "MSMED Act 2006 Section 15",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-014 S.68 Unexplained Cash Credit
    [
        "IT-014", "Statute", "Chapter VI - Set-off, or Carry Forward and Set-off of Loss", "Section 68", "Unexplained Cash Credits (Bank Deposits and Loans)",
        "Where any sum is found credited in the books of an assessee maintained for any previous year, and the assessee offers no explanation about the nature and source thereof or the explanation offered is not satisfactory, the sum so credited may be charged to income-tax.",
        "Section 68 applies when money is credited in the taxpayer's books of accounts (including unexplained bank deposits, share capital, unsecured loans, or gifts) and the taxpayer cannot satisfactorily explain its source. The Assessing Officer can treat this unexplained amount as taxable income. Under Section 115BBE, such unexplained income is taxed at a flat rate of 60% plus 25% surcharge and 4% cess, bringing the effective tax rate to 78%, with no deductions or basic exemption allowed.",
        "Section 68, Unexplained cash credit, unexplained bank deposits, loan from friend tax, S.68, Section 115BBE, 78 percent tax",
        "CIT v. Lovely Balaji Brand", 2008,
        "If the assessee provides the names, addresses, and PANs of the creditors/depositors, the burden shifts to the Revenue; it cannot make additions under S.68 without verification.",
        "NRA Iron & Steel Pvt. Ltd. v. CIT", 2019, "Supreme Court held that the taxpayer must prove: 1. Identity of the creditor; 2. Creditworthiness of the creditor; 3. Genuineness of the transaction, especially for share premium/loans.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Unexplained Income", "Taxed at 78% flat rate under Section 115BBE",
        "No basic exemption limit or business loss set-off can be claimed against S.68 income.", "Section 115BBE, Section 69",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-015 S.69 Unexplained Investments
    [
        "IT-015", "Statute", "Chapter VI - Set-off, or Carry Forward and Set-off of Loss", "Section 69", "Unexplained Investments and Money",
        "Where in the financial year immediately preceding the assessment year, the assessee has made investments which are not recorded in the books of account, and the assessee offers no explanation, the value of the investments may be deemed to be the income.",
        "Section 69 (along with S.69A, 69B, 69C) covers unexplained investments (buying property, gold, shares), unexplained cash, jewelry, or unexplained expenditures not recorded in the books. If the taxpayer cannot prove the source of funds, it is treated as deemed income and taxed at the punitive rate of 78% (60% tax + 25% surcharge + cess) under Section 115BBE, and penalties can also be levied.",
        "Section 69, Unexplained investment, S.69A unexplained money, property purchase cash source, S.115BBE, cash search seizure",
        "CIT v. Smt. P.K. Noorjahan", 1999,
        "The word 'may' in S.69 gives discretion to the Assessing Officer; if the taxpayer has no source of income (e.g. a young student) and the investment is small, it need not automatically be added as income.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Unexplained Income", "Taxed at 78% flat rate under Section 115BBE",
        "Penalty of 10% under S.271AAC if unexplained income is voluntarily declared in ITR; otherwise 60% penalty if detected during audit.", "Section 68, Section 115BBE",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-016 S.54 capital gains exemption house
    [
        "IT-016", "Statute", "Chapter IV - Computation of Total Income", "Section 54", "Capital Gains Exemption on Sale of Residential House",
        "Where the capital gain arises from the transfer of a long-term capital asset, being a residential house, and the assessee has within a period of one year before or two years after purchased, or within three years constructed, a residential house, the gain shall be exempt.",
        "Section 54 provides an exemption on Long-Term Capital Gains (LTCG) arising from the sale of a residential house. To claim the exemption, the gains must be reinvested in another residential house in India. The new house must be purchased within 1 year before or 2 years after the sale, or constructed within 3 years. From FY 2023-24, the maximum capital gains exemption under S.54 is capped at ₹10 Crore. If the money is not fully utilized before the ITR filing due date, it must be deposited in the Capital Gains Accounts Scheme (CGAS).",
        "Section 54, Capital gains house sale, capital gains account scheme, CGAS, reinvestment home, LTCG exemption property, S.54",
        "CIT v. Podar Cement Pvt. Ltd.", 1997,
        "Established that actual control and beneficial ownership is key, even if registration of the new property is pending.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Capital Gains Exemption", "100% of capital gains up to a maximum cap of ₹10 Crore",
        "The new property must not be sold within 3 years from its purchase/construction date; otherwise, the exempted gain is deducted from its cost price when computing tax on the new sale.", "Section 54F, Section 54EC",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-017 S.54EC Capital Gains Bonds
    [
        "IT-017", "Statute", "Chapter IV - Computation of Total Income", "Section 54EC", "Capital Gains Exemption via S.54EC Bonds",
        "Where the capital gain arises from the transfer of a long-term capital asset, being land or building or both, and the assessee has within a period of six months invested the whole or any part of capital gains in the long-term specified asset.",
        "Section 54EC offers a way to save tax on Long-Term Capital Gains (LTCG) arising from the sale of land or building by investing the gains in specified NHAI, REC, PFC, or IRFC bonds. The investment must be made within 6 months of the sale date. The bonds have a lock-in period of 5 years. The maximum investment limit is ₹50 Lakhs per financial year.",
        "Section 54EC, Capital gains bonds, NHAI bonds capital gains, REC bonds saving tax, 5 year lock-in property sale, S.54EC",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2000, "Ministry of Finance - CBDT",
        "Capital Gains Exemption", "Maximum investment of ₹50 Lakhs (tax exemption matching amount invested)",
        "Bonds cannot be transferred, sold, or pledged as security for a loan within 5 years; doing so makes the exempted gain taxable.", "Section 54, Section 54F",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-018 S.54F Exemption on other assets
    [
        "IT-018", "Statute", "Chapter IV - Computation of Total Income", "Section 54F", "Capital Gains Exemption on Sale of Other Assets (Shares, Gold etc.)",
        "Where the capital gain arises from the transfer of any long-term capital asset, not being a residential house, and the assessee has within a period of one year before or two years after purchased, or within three years constructed, a residential house.",
        "Section 54F provides an exemption on Long-Term Capital Gains (LTCG) from the sale of any asset *other than* a residential house (such as equity shares, mutual funds, gold, commercial property). To claim this exemption, the entire *net sale consideration* (not just the capital gain) must be reinvested in purchasing or constructing one residential house in India. The purchase/construction timelines are the same as S.54. The maximum exemption is capped at ₹10 Crore, and the taxpayer must not own more than one residential house on the date of transfer.",
        "Section 54F, Save tax on gold sale, capital gains shares property, reinvest net consideration house, S.54F, gold capital gains",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1982, "Ministry of Finance - CBDT",
        "Capital Gains Exemption", "Proportionate exemption based on net consideration reinvested, capped at ₹10 Crore",
        "The taxpayer must not buy another house within 2 years or construct another within 3 years of the transfer date.", "Section 54, Section 54EC",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-019 S.269SS Cash loan restriction
    [
        "IT-019", "Statute", "Chapter XX-B - Requirement as to Mode of Acceptance, Payment or Repayment in Certain Cases", "Section 269SS", "Restrictions on Accepting Cash Loans and Deposits above 20,000",
        "No person shall take or accept from any other person, any loan or deposit or any specified sum, otherwise than by an account payee cheque or account payee bank draft or use of electronic clearing system, if the amount is twenty thousand rupees or more.",
        "Section 269SS prohibits accepting loans, deposits, or advances for transfer of immovable property in cash if the total amount is ₹20,000 or more. Any transaction of ₹20,000 or above must be done through banking channels (cheque, draft, net banking, UPI, cards). If violated, a penalty equal to 100% of the loan amount is levied under S.271D.",
        "Section 269SS, Cash loan limit, cash deposit 20000, friend loan cash penalty, Section 271D penalty, cash property advance, S.269SS",
        "Assistant Director of Inspection (Investigation) v. Kum. A.B. Shanthi", 2002,
        "Supreme Court upheld the constitutionality of S.269SS. It was enacted to prevent tax evaders from explaining away unaccounted cash discovered during search operations as loans from friends.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1984, "Ministry of Finance - CBDT",
        "Cash Transactions Restrictions", "100% penalty on the amount accepted in cash",
        "Does not apply if both the giver and receiver have agricultural income and no other taxable income.", "Section 269T, Section 271D",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-020 S.269T Cash loan repayment restriction
    [
        "IT-020", "Statute", "Chapter XX-B - Requirement as to Mode of Acceptance, Payment or Repayment in Certain Cases", "Section 269T", "Restrictions on Repaying Loans and Deposits in Cash",
        "No branch of a banking company or a co-operative bank and no other person shall repay any loan or deposit made with it or any specified sum otherwise than by an account payee cheque or account payee bank draft, if the amount is twenty thousand rupees or more.",
        "Section 269T prohibits repaying any loan, deposit, or property advance in cash if the amount is ₹20,000 or more. If a person repays ₹20,000 or more in cash, they face a 100% penalty of the repaid amount under Section 271E.",
        "Section 269T, Cash loan repayment limit, repaying cash penalty, cash bank deposit withdrawal, Section 271E penalty, S.269T",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1981, "Ministry of Finance - CBDT",
        "Cash Transactions Restrictions", "100% penalty on the amount repaid in cash under Section 271E",
        "Does not apply if the loan is repaid to the government, banking company, or government corporations.", "Section 269SS, Section 271E",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-021 S.10(10D) Life Insurance maturity
    [
        "IT-021", "Statute", "Chapter II - Incomes which do not form part of Total Income", "Section 10(10D)", "Taxability of Life Insurance Policy Maturity Payouts",
        "Any sum received under a life insurance policy, including the sum allocated by way of bonus on such policy, is exempt from tax, subject to certain conditions.",
        "Section 10(10D) provides that maturity proceeds of a life insurance policy are tax-free, EXCEPT in these cases: 1. If premium in any year exceeds 10% of sum assured (for policies bought after April 2012; 20% for older policies). 2. For ULIPs (Unit Linked Insurance Plans) bought after Feb 2021, if annual premium exceeds ₹2.5 Lakhs. 3. For traditional plans bought after 1 April 2023, if aggregate annual premium exceeds ₹5 Lakhs. In case of the policyholder's death, the entire death benefit remains fully tax-free regardless of premium amounts.",
        "Section 10(10D), Life insurance tax maturity, LIC tax free proceeds, sum assured 10 percent, traditional plan 5 lakh premium, ULIP tax limit, S.10(10D)",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Exemptions", "Fully exempt unless premium limits are breached",
        "Death benefits are always tax-free without any threshold limit.", "Section 80C",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-022 S.56(2)(x) Taxation of gifts
    [
        "IT-022", "Statute", "Chapter IV - Computation of Total Income", "Section 56(2)(x)", "Taxation of Gifts Received by Individuals",
        "Where any person receives, in any previous year, from any person or persons on or after the 1st day of April, 2017 - (a) any sum of money, without consideration, the aggregate value of which exceeds fifty thousand rupees.",
        "Section 56(2)(x) governs tax on gifts (cash, property, jewelry, shares). If aggregate value of gifts from non-relatives exceeds ₹50,000 in a year, the entire value is taxed as 'Income from Other Sources' under slabs. Exemptions (no tax at all): 1. Gifts from relatives (spouse, parents, siblings, children, lineage ancestors/descendants). 2. Gifts received on marriage. 3. Gifts received under a will or inheritance. 4. Gifts from local authorities, registered trusts.",
        "Section 56(2)(x), Gift tax limit, cash gift relative tax exemption, marriage gifts tax, property gift from friend, S.56(2)(x)",
        "CIT v. M/s Sarika", 2013,
        "Established that gift transactions between non-relatives must show valid love and affection to be genuine, otherwise taxed.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2017, "Ministry of Finance - CBDT",
        "Income from Other Sources", "Taxed under standard individual slabs if total exceeds ₹50,000",
        "Gifts from defined relatives are fully exempt without any upper limit.", "Section 56(2)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-023 S.50C Capital gains stamp duty valuation
    [
        "IT-023", "Statute", "Chapter IV - Computation of Total Income", "Section 50C", "Capital Gains Stamp Duty Valuation (Circle Rate)",
        "Where the consideration received or accruing as a result of the transfer of a capital asset, being land or building or both, is less than the value adopted by any authority of a State Government for the purpose of payment of stamp duty, the value so adopted shall be deemed to be the full value.",
        "Section 50C applies to sale of land or building. If the declared sale price is lower than the State Government's circle rate (stamp duty value), the circle rate is treated as the sale price to compute capital gains tax. However, a safe harbor limit of 10% is allowed: if the stamp duty value does not exceed 110% of the actual transaction price, the actual transaction price is accepted as the sale price.",
        "Section 50C, Stamp duty value capital gains, circle rate sale price tax, 110 percent safe harbor property, S.50C",
        "CIT v. Reliance Petroproducts Pvt. Ltd.", 2010,
        "Valuations by government authorities are presumed correct unless disputed before valuation officers.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2002, "Ministry of Finance - CBDT",
        "Capital Gains Tax Rules", "Deemed sale consideration matches stamp duty value if transaction is undervalued",
        "Allows taxpayer to request reference to a Valuation Officer if they claim actual market value is lower than circle rate.", "Section 43CA, Section 56(2)(x)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-024 S.194IA TDS on property sale
    [
        "IT-024", "Statute", "Chapter XVII - Collection and Recovery of Tax", "Section 194-IA", "TDS on Sale of Immovable Property",
        "Any person, being a transferee, responsible for paying to a resident transferor any sum by way of consideration for transfer of any immovable property shall, at the time of credit or payment, deduct an amount equal to one per cent of such sum as income-tax.",
        "Section 194-IA mandates that the buyer of immovable property (land or building, other than agricultural land) costing ₹50 Lakhs or more must deduct 1% TDS from the sale price before paying the seller. The buyer must deposit this TDS using Form 26QB using the seller's PAN. Seller can claim credit for this TDS during filing. If the seller does not provide a PAN, the TDS rate increases to 20%.",
        "Section 194-IA, TDS on property purchase 50 Lakhs, Form 26QB property TDS, 1 percent TDS land house, S.194-IA",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2013, "Ministry of Finance - CBDT",
        "TDS / TCS Provisions", "1% of total transaction value (20% if no PAN provided)",
        "Does not apply to agricultural land.", "Section 194-IB, Form 26QB",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-025 S.194IB TDS on rent by individuals
    [
        "IT-025", "Statute", "Chapter XVII - Collection and Recovery of Tax", "Section 194-IB", "TDS on Rent Paid by Individuals and HUFs",
        "Any person, being an individual or a Hindu undivided family (other than those referred to in S.194I), responsible for paying to a resident any income by way of rent exceeding fifty thousand rupees for a month shall deduct five per cent.",
        "Section 194-IB mandates that individuals or HUFs who pay rent exceeding ₹50,000 per month for residential or commercial property must deduct 5% TDS from the rent. The TDS must be deducted once a year (at the end of the FY or when vacating the property) and deposited using Form 26QC. This TDS does not require a TAN (Tax Deduction Account Number); the buyer can use their PAN.",
        "Section 194-IB, TDS on rent above 50000, Form 26QC rent TDS, individual pay rent TDS, S.194-IB",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2017, "Ministry of Finance - CBDT",
        "TDS / TCS Provisions", "5% of total rent paid in a financial year (20% if no PAN provided)",
        "TAN is not required; payment and return are combined in Form 26QC.", "Section 194-I, Form 26QC",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-026 S.206C(1G) TCS on LRS / Foreign Travel
    [
        "IT-026", "Statute", "Chapter XVII - Collection and Recovery of Tax", "Section 206C(1G)", "TCS on Foreign Remittances (LRS) and Tour Packages",
        "Every person, being an authorised dealer, who receives an amount, for remittance out of India from a buyer, being a person remitting such amount under the Liberalised Remittance Scheme shall collect TCS.",
        "Section 206C(1G) governs Tax Collected at Source (TCS) on foreign remittances under RBI's Liberalised Remittance Scheme (LRS) and overseas tour packages. Effective from 1 October 2023: 1. Overseas Tour Packages: 5% TCS up to ₹7 Lakhs, and 20% TCS on amounts above ₹7 Lakhs. 2. Other Remittances (except Education/Medical): Nil up to ₹7 Lakhs, and 20% TCS above ₹7 Lakhs. 3. Education Loans: 0.5% TCS above ₹7 Lakhs.",
        "Section 206C(1G), TCS on foreign travel, LRS foreign remittance TCS, 20 percent TCS, sending money abroad tax, S.206C(1G)",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2020, "Ministry of Finance - CBDT",
        "TDS / TCS Provisions", "5% or 20% TCS depending on purpose and limit",
        "TCS is not an additional tax; it can be claimed as a credit or refund while filing the annual income tax return.", "Section 192",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-027 S.44AE Presumptive tax for transporters
    [
        "IT-027", "Statute", "Chapter IV - Profits and Gains of Business or Profession", "Section 44AE", "Presumptive Taxation for Goods Transporters",
        "Notwithstanding anything to the contrary contained in sections 28 to 43C, in the case of an assessee, who owns not more than ten goods carriages and who is engaged in the business of plying, hiring or leasing.",
        "Section 44AE provides a presumptive tax scheme for small goods transporters owning 10 or fewer trucks/goods carriages. The taxable income is calculated on a flat rate basis: 1. Heavy Goods Vehicle (capacity > 12,000 kg): ₹1,000 per metric ton of gross vehicle weight for every month or part of a month. 2. Other Vehicles: ₹7,500 per month or part of a month. Genuinely no need to maintain books of accounts or undergo tax audit.",
        "Section 44AE, Transporter presumptive tax, truck owner tax scheme, 7500 per month vehicle, S.44AE",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Medium", "Income Tax Law", 1994, "Ministry of Finance - CBDT",
        "Profits and Gains of Business or Profession", "Fixed presumptive income per month of vehicle ownership",
        "Assessee must own 10 or fewer vehicles during the entire previous year.", "Section 44AD",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-028 PAN-Aadhaar linking S.139AA
    [
        "IT-028", "Statute", "Chapter XIV - Procedure for Assessment", "Section 139AA", "Mandatory PAN-Aadhaar Linking",
        "Every person who has been allotted a permanent account number as on the 1st day of July, 2017, and who is eligible to obtain Aadhaar number, shall intimate his Aadhaar number.",
        "Section 139AA makes it mandatory to link PAN (Permanent Account Number) with Aadhaar. If a taxpayer fails to link them by the government's deadline (which was 30 June 2023), the PAN becomes 'inoperative'. Consequences of an inoperative PAN: 1. Taxpayer cannot file ITR; 2. Pending refunds are not processed; 3. TDS is deducted at double/punitive rates (usually 20%). A late fee of ₹1,000 must be paid to link the PAN-Aadhaar.",
        "Section 139AA, PAN Aadhaar linking mandatory, inoperative PAN consequences, link PAN fee 1000, double TDS PAN, S.139AA",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2017, "Ministry of Finance - CBDT",
        "Assessment Procedure", "PAN becomes inoperative if not linked; fee of ₹1,000 to reactivate",
        "Exemptions: NRI, non-citizens, individuals aged 80+ years, and residents of Assam, Jammu & Kashmir, and Meghalaya.", "Section 206AA",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-029 Set-off of losses S.71/72
    [
        "IT-029", "Statute", "Chapter VI - Set-off, or Carry Forward and Set-off of Loss", "Section 71 & 72", "Set-off and Carry Forward of Losses",
        "Where in respect of any assessment year the net result of the computation under any head of income... is a loss, the assessee shall be entitled to have the amount of such loss set off.",
        "Section 71 & 72 govern how losses can be offset against other income. 1. House Property Loss: Can be set off against any other income up to ₹2,00,000 per year; excess can be carried forward for 8 years (and set off only against house property income). 2. Business Loss: Cannot be set off against Salary income; can carry forward for 8 years. 3. Capital Losses: Short-term capital loss can be set off against both STCG and LTCG; Long-term capital loss can *only* be set off against LTCG. Capital losses can carry forward for 8 years.",
        "Section 71, Business loss set off salary, house property loss limit 2 lakh, carry forward losses 8 years, short term capital loss set off, S.71, S.72",
        "CIT v. Harprasad & Co. Pvt. Ltd.", 1975,
        "Established that if an income is exempt from tax, the loss from that source cannot be set off against other taxable income.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 1961, "Ministry of Finance - CBDT",
        "Set-off and Carry Forward rules", "Strict set-off limits as specified per head of income",
        "Losses cannot be carried forward if the ITR is filed after the due date (except for house property loss).", "Section 139(1)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ],
    # IT-030 S.234F Late filing fee
    [
        "IT-030", "Statute", "Chapter XVII - Collection and Recovery of Tax", "Section 234F", "Late Filing Fee for Income Tax Return (ITR)",
        "Without prejudice to the provisions of this Act, where a person required to furnish a return of income under section 139, fails to do so within the time prescribed, he shall pay by way of fee.",
        "Section 234F mandates a late fee if the Income Tax Return (ITR) is filed after the statutory due date (usually 31 July for individuals). Slabs: 1. If total taxable income is ₹5 Lakhs or less: Late fee is ₹1,000. 2. If total taxable income exceeds ₹5 Lakhs: Late fee is ₹5,000. This fee must be paid before submitting the delayed return.",
        "Section 234F, ITR late fee 5000, late filing fee 1000, delayed tax return penalty, July 31 deadline penalty, S.234F",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "Income Tax Law", 2017, "Ministry of Finance - CBDT",
        "Penalties / Late Fees", "₹1,000 or ₹5,000 depending on taxable income",
        "No fee is payable if total gross income does not exceed the basic exemption limit.", "Section 139(1)",
        "Legislative Enactment", "In force", "https://www.incometax.gov.in/", "Income Tax Act, 1961", "Active"
    ]
]

gst_rows = [
    # GST-001 Art 246A
    [
        "GST-001", "Statute", "Constitutional Foundation", "Article 246A", "Special Provision for Goods and Services Tax",
        "Parliament and, subject to clause (2), the Legislature of every State, have power to make laws with respect to goods and services tax imposed by the Union or by such State.",
        "Article 246A of the Indian Constitution was introduced by the 101st Amendment in 2016. It gives concurrent powers to both the Parliament of India and the State Legislatures to make laws regarding Goods and Services Tax (GST). Parliament has exclusive power for interstate supply of goods or services (IGST).",
        "Article 246A, Constitutional Amendment, Concurrent power, IGST CGST SGST, GST Constitution",
        "Mohit Minerals Pvt. Ltd. v. Union of India", 2022,
        "Determined that the recommendations of the GST Council are not binding on Parliament and States; Article 246A gives both equal law-making powers, and GST Council decisions have persuasive value.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2016, "Ministry of Finance - CBIC",
        "Constitutional Provision", "Not Applicable / N.A.",
        "Subject to joint consensus through the GST Council.", "Article 279A",
        "Constitutional Amendment", "In force", "https://www.indiacode.nic.in/", "Constitution of India", "Active"
    ],
    # GST-002 GST Council Art 279A
    [
        "GST-002", "Statute", "Constitutional Foundation", "Article 279A", "GST Council — Composition and Functions",
        "The President shall, within sixty days from the date of commencement of the Constitution (One Hundred and First Amendment) Act, 2016, by order, constitute a Council to be called the Goods and Services Tax Council.",
        "Article 279A authorizes the creation of the GST Council. It is headed by the Union Finance Minister and includes the Union Minister of State for Revenue and Finance Ministers of all State Governments. The Council decides GST rates, exemptions, thresholds, and administrative rules. Decisions require a 3/4ths majority: the Centre holds 1/3rd voting weight, and all States combined hold 2/3rds.",
        "Article 279A, GST Council, Voting weight, Finance Minister, GST rate decision",
        "Mohit Minerals Pvt. Ltd. v. Union of India", 2022,
        "Established that recommendations of the GST Council are persuasive and meant to promote cooperative federalism.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2016, "Ministry of Finance - CBIC",
        "Constitutional Provision", "Not Applicable / N.A.",
        "Decisions must be made by 75% weighted majority vote.", "Article 246A",
        "Constitutional Amendment", "In force", "https://www.indiacode.nic.in/", "Constitution of India", "Active"
    ],
    # GST-003 S.7 CGST Act Scope of Supply
    [
        "GST-003", "Statute", "Levy and Collection of Tax", "Section 7", "Scope of Supply in GST",
        "For the purposes of this Act, the expression supply includes all forms of supply of goods or services or both such as sale, transfer, barter, exchange, licence, rental, lease or disposal made or agreed to be made for a consideration by a person in the course or furtherance of business.",
        "Section 7 of the CGST Act defines what constitutes a 'supply', which is the taxable event in GST. It includes sale, transfer, barter, exchange, lease, or license of goods or services done for a consideration in the course of business. It also covers import of services (even without consideration in specific cases under Schedule I).",
        "Section 7, Scope of Supply, Taxable Event, Consideration, Business furtherance, Schedule I, S.7 CGST",
        "Commissioner of Service Tax v. M/s Quick Heal Technologies Ltd.", 2022,
        "Clarified distinction between sale of software goods vs supply of services under indirect tax statutes.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Levy and Collection", "Tax is levied on transaction value under Section 15",
        "Transactions without consideration are not supplies unless covered under Schedule I.", "Section 9 CGST Act, Schedule I, II, III",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-004 S.22 CGST Act Registration
    [
        "GST-004", "Statute", "Registration", "Section 22", "Threshold for GST Registration",
        "Every supplier shall be liable to be registered under this Act in the State or Union territory, other than special category States, from where he makes a taxable supply of goods or services or both, if his aggregate turnover in a financial year exceeds twenty lakh rupees.",
        "Section 22 sets the aggregate turnover limits above which GST registration is mandatory. 1. For Suppliers of Goods: ₹40 Lakhs (reduced to ₹20 Lakhs in Special Category/Hill States). 2. For Suppliers of Services: ₹20 Lakhs (reduced to ₹10 Lakhs in Special Category States). Aggregate turnover is calculated pan-India and includes taxable, exempt, and export supplies.",
        "Section 22, GST Registration Threshold, Aggregate Turnover, 40 Lakhs, 20 Lakhs, S.22 CGST",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Registration requirements", "Penalty of 10,000 or tax evaded under Section 122 if operating unregistered above threshold",
        "Does not apply if the taxpayer falls under Section 24 (compulsory registration regardless of turnover).", "Section 23, Section 24",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-005 S.24 Compulsory Registration
    [
        "GST-005", "Statute", "Registration", "Section 24", "Compulsory GST Registration",
        "Notwithstanding anything contained in sub-section (1) of section 22, the following categories of persons shall be required to be registered under this Act.",
        "Section 24 lists cases where GST registration is compulsory, meaning the ₹20L/₹40L threshold exemption does not apply. Key categories: 1. Persons making interstate taxable supplies; 2. Casual Taxable Persons (CTPs); 3. Non-Resident Taxable Persons (NRTPs); 4. E-commerce operators and suppliers selling through them; 5. Persons liable to pay tax under Reverse Charge (RCM); 6. Input Service Distributors (ISDs).",
        "Section 24, Compulsory Registration, Interstate supply, E-commerce, Reverse Charge, S.24 CGST",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Registration requirements", "Compulsory registration required before starting business operations",
        "Interstate suppliers of services are exempt from compulsory registration if aggregate turnover is under 20 lakhs.", "Section 22, Section 25",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-006 S.16 Eligibility for Input Tax Credit
    [
        "GST-006", "Statute", "Input Tax Credit", "Section 16", "Eligibility and Conditions for Claiming ITC",
        "Every registered person shall, subject to such conditions and restrictions as may be prescribed, be entitled to take credit of input tax charged on any supply of goods or services or both to him which are used or intended to be used in the course or furtherance of his business.",
        "Section 16 lists the 4 core conditions to claim Input Tax Credit (ITC): 1. Taxpayer must possess a tax invoice or debit note; 2. Goods or services must have been actually received; 3. The supplier must have actually paid the tax collected to the government; 4. The taxpayer must have filed their GST return (GSTR-3B). Additionally, S.16(2)(aa) mandates that the invoice must be uploaded by the supplier in GSTR-1 and reflect in the buyer's GSTR-2B.",
        "Section 16, Input Tax Credit, ITC Eligibility, GSTR-2B reconciliation, S.16 CGST, Conditions for ITC",
        "Union of India v. Filco Trade Centre Pvt. Ltd.", 2022,
        "Directed the CBIC to open the portal for filing transitional ITC claims (TRAN-1/TRAN-2) to ensure taxpayers did not lose pre-GST credits.",
        "M/s D.Y. Beathel Enterprises v. State Tax Officer", 2021, "Madras HC held that if the buyer has paid tax to the seller, the tax dept should recover from the seller if they defaulted on payment before denying ITC to the buyer.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Input Tax Credit Rules", "Denial of ITC and interest at 18% on wrong claims under Section 50",
        "ITC must be reversed if payment to the supplier is not made within 180 days from the invoice date.", "Section 17(5) (Blocked Credits), Section 49",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-007 S.17(5) Blocked Credits
    [
        "GST-007", "Statute", "Input Tax Credit", "Section 17(5)", "Blocked Input Tax Credits (Ineligible ITC)",
        "Input tax credit shall not be available in respect of the following, namely: (a) motor vehicles for transportation of persons having approved seating capacity of not more than thirteen persons...",
        "Section 17(5) lists goods and services on which Input Tax Credit (ITC) is 'blocked' (not allowed), even if used for business. 1. Motor Vehicles: Seating capacity <= 13 (allowed only if used for driving school, transport of passengers, or resale). 2. Personal Consumption: Food and beverages, outdoor catering, beauty treatment, health services, life/health insurance, club membership, travel benefits. 3. Works Contract: Services and goods for construction of immovable property (except plant & machinery). 4. Lost/Stolen: Goods lost, stolen, destroyed, written off, or given as gifts.",
        "Section 17(5), Blocked Credit, Ineligible ITC, Food Catering, Works Contract construction, S.17(5) CGST",
        "Safari Retreats Pvt. Ltd. v. Chief Commissioner of CGST", 2019,
        "Orissa HC held that ITC on inputs used for construction of a shopping mall meant for letting out is admissible, as it is in furtherance of business; appealed to Supreme Court.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Input Tax Credit Rules", "Ineligible ITC must be self-reversed in GSTR-3B to avoid penalty",
        "Deduction is allowed if inputs are used for making outward taxable supplies of the same category (e.g., subcontractor in works contract).", "Section 16",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-008 S.73 CGST Act Demand for Non-Fraud
    [
        "GST-008", "Statute", "Demands and Recovery", "Section 73", "GST Demand and Show Cause Notice in Non-Fraud Cases",
        "Where it appears to the proper officer that any tax has not been paid or short paid or erroneously refunded, or where input tax credit has been wrongly availed or utilised for any reason, other than the reason of fraud or any wilful-misstatement or suppression of facts to evade tax, he shall serve notice.",
        "Section 73 governs tax demands where there is NO fraud, suppression of facts, or intent to evade tax. If tax is unpaid/short paid or ITC is wrongly claimed, the officer issues a Show Cause Notice (SCN). Taxpayer can pay the tax amount + interest before the SCN, or within 30 days of the SCN, to get a waiver of penalty. Penalty is capped at 10% of the tax or ₹10,000 (whichever is higher) if paid later. SCN must be issued at least 3 months before the 3-year time limit for passing the order.",
        "Section 73, GST SCN, Show cause notice non fraud, penalty waiver GST, 3 year time limit SCN, S.73 CGST Act",
        "Union of India v. Filco Trade Centre Pvt. Ltd.", 2022,
        "Established procedural timelines for tax claims; tax departments must adhere strictly to statutory notice windows.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Demands and Recovery", "Penalty of 10% of tax or ₹10,000, whichever is higher, in case of delay beyond SCN response window",
        "Does not apply if there is evidence of fraud or suppression of facts (in which case S.74 applies).", "Section 74, Section 50, Section 75",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-009 S.74 CGST Act Demand for Fraud
    [
        "GST-009", "Statute", "Demands and Recovery", "Section 74", "GST Demand and Show Cause Notice in Fraud Cases",
        "Where it appears to the proper officer that any tax has not been paid or short paid or erroneously refunded, or where input tax credit has been wrongly availed or utilised by reason of fraud or any wilful-misstatement or suppression of facts to evade tax, he shall serve notice.",
        "Section 74 governs tax demands when there is fraud, willful misstatement, or suppression of facts to evade tax. The time limit for passing the recovery order is longer: 5 years from the return filing due date. SCN must be issued at least 6 months before the 5-year limit. Penalties are much higher: 100% of the tax evaded. If paid within 30 days of SCN, penalty is reduced to 25%; if paid within 30 days of the final order, penalty is reduced to 50%.",
        "Section 74, GST Fraud SCN, tax evasion penalty, suppression of facts, 5 year time limit, 100 percent penalty, S.74 CGST Act",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Demands and Recovery", "Penalty up to 100% of the tax evaded",
        "Requires clear proof of intent to evade tax; officers cannot invoke S.74 for bona fide interpretative errors.", "Section 73, Section 75",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-010 S.50 Interest on late payment
    [
        "GST-010", "Statute", "Payment of Tax", "Section 50", "Interest on Delayed Payment of GST",
        "Every person who is liable to pay tax in accordance with the provisions of this Act or the rules made thereunder, but fails to pay the tax... shall for the period for which the tax or any part thereof remains unpaid, pay on his own accord interest.",
        "Section 50 governs interest on late payment of GST. Effective interest is: 1. 18% per annum for late payment of tax; 2. 24% per annum for undue or excess claim of Input Tax Credit (ITC). Critically, interest is payable only on the 'net cash liability' (i.e. the tax paid through the cash ledger) and not on the portion paid using ITC balance, provided the return is filed before recovery proceedings begin.",
        "Section 50, Interest on late GST, net tax liability interest, 18 percent interest, 24 percent ITC interest, delayed GSTR-3B, S.50 CGST Act",
        "Union of India v. Bharti Airtel Ltd.", 2021,
        "Supreme Court ruled on net tax liability and adjustments of ITC records, establishing limits of retrospective correction.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Payment of Tax Interest", "18% per annum on net cash tax liability; 24% per annum on wrongly utilized ITC",
        "Interest is not payable on unutilized ITC lying in the electronic credit ledger.", "Section 49",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-011 S.129 E-way bill detention
    [
        "GST-011", "Statute", "Offences and Penalties", "Section 129", "Detention and Seizure of Goods in Transit (E-way Bill Violations)",
        "Notwithstanding anything contained in this Act, where any person transports any goods or stores any goods while they are in transit in contravention of the provisions of this Act or the rules made thereunder, all such goods and conveyance shall be liable to detention or seizure.",
        "Section 129 governs the detention of goods and vehicles in transit (usually for carrying goods without an E-way bill, or with an expired/incorrect E-way bill). To release the seized goods: 1. If owner comes forward: Penalty is 200% of the tax payable on the goods. 2. If owner does not come forward: Penalty is 50% of the value of goods or 200% of the tax, whichever is higher. Vehicles must be released on payment of penalty or ₹1 Lakh, whichever is lower.",
        "Section 129, Eway bill penalty, expired eway bill, goods seized transit, 200 percent penalty GST, vehicle detention, S.129 CGST Act",
        "Assistant Commissioner v. M/s Satyam Shivam Papers Pvt. Ltd.", 2022,
        "Supreme Court held that tax authorities cannot levy penalties under S.129 if there is no intent to evade tax and the delay in transport was due to traffic blockages/force majeure.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Transit Penalties", "200% of tax or 50% of goods value depending on ownership declaration",
        "Proper officer must issue notice of detention within 7 days of interception and pass order within 7 days of notice.", "Section 130, Rule 138",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-012 S.132 Arrest provisions
    [
        "GST-012", "Statute", "Offences and Penalties", "Section 132", "Arrest and Criminal Prosecution in GST",
        "Whoever commits any of the following offences, namely: (a) supplies any goods or services without issue of any invoice; (b) issues any invoice without supply of goods or services leading to wrongful availment of input tax credit... shall be punishable.",
        "Section 132 details offenses that attract arrest and jail time. Key criteria: 1. Tax evasion or fake ITC amount > ₹5 Crore: Cognizable and Non-Bailable (prison up to 5 years). 2. Amount between ₹2 Crore and ₹5 Crore: Non-Cognizable and Bailable (prison up to 3 years). 3. Amount between ₹1 Crore and ₹2 Crore: Prison up to 1 year. The law targets circular trading, issuing fake invoices without actual supply, and hiding sales.",
        "Section 132, Fake invoice arrest GST, tax evasion threshold, non bailable GST offenses, prison time tax fraud, S.132 CGST Act",
        "C. Pradeep v. Commissioner of GST", 2019,
        "Supreme Court indicated that pre-arrest bail can be granted if the taxpayer cooperates with the investigation and deposit of partial tax liability is arranged.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Criminal Prosecution", "Imprisonment up to 5 years and fine depending on the amount evaded",
        "Prior sanction of the Commissioner is mandatory before arrest.", "Section 138 (Compounding of offences)",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-013 S.10 Composition scheme
    [
        "GST-013", "Statute", "Levy and Collection of Tax", "Section 10", "GST Composition Scheme S.10",
        "Notwithstanding anything to the contrary contained in this Act but subject to the provisions of sub-sections (3) and (4) of S.9, a registered person, whose aggregate turnover in the preceding financial year did not exceed one crore and fifty lakh rupees, may opt to pay tax.",
        "Section 10 offers a simplified Composition Scheme for small businesses with an aggregate annual turnover up to ₹1.5 Crore (₹75 Lakhs for special category states). Rates: 1. Manufacturers and Traders: 1% of turnover (0.5% CGST + 0.5% SGST); 2. Restaurants (not serving alcohol): 5% of turnover (2.5% CGST + 2.5% SGST); 3. Service Providers: 6% of turnover under Composition (up to ₹50 Lakhs limit). Taxpayers under this scheme cannot collect tax from customers, cannot claim Input Tax Credit (ITC), and cannot make interstate outward supplies.",
        "Section 10, GST composition scheme rate, composition limit 1.5 crore, small business GST option, composition tax invoice, S.10 CGST Act",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Levy and Collection", "Fixed lower tax rate on turnover without ITC eligibility",
        "Cannot be opted by manufacturers of ice cream, pan masala, tobacco, or aerated water, or e-commerce suppliers.", "Section 9",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-014 S.29 Cancellation of GST
    [
        "GST-014", "Statute", "Registration", "Section 29", "Cancellation of GST Registration",
        "The proper officer may, either on his own motion or on an application filed by the registered person or by his legal heirs, cancel the registration, in such manner and within such period as may be prescribed.",
        "Section 29 governs the cancellation of GST registration. It can be initiated: 1. By Taxpayer (e.g. business closed, partners died, turnover fell below limits). 2. By GST Officer (if returns not filed for 6 consecutive months, or composition dealer has not filed returns for 3 quarters, or registration obtained by fraud). Once cancelled, the business must pay tax matching input credit on stock held, or output tax, whichever is higher.",
        "Section 29, GST registration cancellation, suspension of GSTIN, officer cancel GST return non filing, close business GST, S.29 CGST Act",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Registration requirements", "Requires filing of final return GSTR-10 within 3 months of cancellation",
        "Cancellation does not affect tax liability accrued prior to the date of cancellation.", "Section 30 (Revocation), Section 22",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-015 S.30 Revocation of cancellation
    [
        "GST-015", "Statute", "Registration", "Section 30", "Revocation of Cancellation of GST Registration",
        "Subject to such conditions as may be prescribed, any registered person, whose registration is cancelled by the proper officer on his own motion, may apply to such officer for revocation of cancellation.",
        "Section 30 allows a taxpayer whose GST registration was cancelled by an officer to apply for 'Revocation' (reactivation). The application must be filed within 30 days from the date of service of the cancellation order (extendable up to 90 days by Joint/Additional Commissioner). Before applying, the taxpayer must clear all pending tax, interest, and late fees, and file all pending returns.",
        "Section 30, Revocation of GST cancellation, reactivate cancelled GSTIN, time limit revocation 30 days, clear pending returns GST, S.30 CGST Act",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Registration requirements", "Subject to approval by the proper officer upon clearing all defaults",
        "Only available if cancellation was initiated on the officer's own motion (not if taxpayer voluntarily cancelled).", "Section 29",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-016 S.34 Credit and Debit Notes
    [
        "GST-016", "Statute", "Tax Invoice, Credit and Debit Notes", "Section 34", "GST Credit Notes and Debit Notes",
        "Where one or more tax invoices have been issued for supply of goods or services... and the taxable value or tax charged in that tax invoice is found to exceed the taxable value or tax payable, the registered person may issue to the recipient one or more credit notes.",
        "Section 34 regulates Credit Notes and Debit Notes. 1. Credit Note: Issued by the supplier to reduce their tax liability if the invoice value was higher than actual, or if goods are returned, or if services are deficient. 2. Debit Note: Issued by the supplier to increase their tax liability if the invoice value was lower than actual. Credit notes for a financial year must be declared in returns by 30th November of the next financial year.",
        "Section 34, Credit Note GST, Debit Note GST, return of goods tax adjustment, late billing tax, S.34 CGST Act",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Documentation / Adjustments", "Reduction of output tax liability matching Credit Notes",
        "Recipient must reverse equivalent Input Tax Credit when a Credit Note is issued.", "Section 31 (Tax Invoice)",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-017 S.54 GST Refunds
    [
        "GST-017", "Statute", "Refunds", "Section 54", "Refund of GST (Exports and Inverted Duty Structure)",
        "Any person claiming refund of any tax and interest, if any, paid on such tax or any other amount paid by him, may make an application before the expiry of two years from the relevant date.",
        "Section 54 governs the refund of accumulated GST. Common scenarios: 1. Export of goods/services under Letter of Undertaking (LUT) without payment of tax. 2. Inverted Duty Structure (where tax rate on input raw materials is higher than tax rate on finished output goods). 3. Refund of excess balance in the electronic cash ledger. The refund application must be submitted within 2 years from the 'relevant date' (e.g. date of export or return filing due date).",
        "Section 54, GST refund application, inverted duty structure refund, export without tax LUT, relevant date refund, S.54 CGST Act",
        "Union of India v. Mohit Minerals Pvt. Ltd.", 2018,
        "Supreme Court ruled on the constitutional validity of compensation cess and refund rules in transition.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Refund Rules", "Refund released within 60 days of application; S.56 interest applies for delay",
        "No refund is granted if the amount is less than ₹1,000.", "Section 56 (Interest on delayed refund)",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ],
    # GST-018 S.107 Appeals to Appellate Authority
    [
        "GST-018", "Statute", "Appeals and Revision", "Section 107", "Appeals to Appellate Authority under GST",
        "Any person aggrieved by any decision or order passed under this Act or the State Goods and Services Tax Act... may appeal to such Appellate Authority as may be prescribed within three months.",
        "Section 107 gives taxpayers the right to appeal orders passed by GST officers to the first Appellate Authority (e.g. Commissioner Appeals). Time limit to file an appeal is 3 months from the date of the order (4 months for the department). To file the appeal, the taxpayer must pay a mandatory 'pre-deposit' of 10% of the disputed tax amount, which stays the recovery of the remaining 90% of the tax.",
        "Section 107, GST appeal time limit, pre-deposit 10 percent GST, stay on tax recovery, commissioner appeals, S.107 CGST Act",
        "Singh Enterprises v. Commissioner of Central Excise", 2008,
        "Established that statutory limits for filing appeals cannot be extended by courts beyond the condonable period specified in the Act.",
        "Not Applicable / N.A.", 0, "Not Applicable / N.A.",
        "High", "GST Law", 2017, "Ministry of Finance - CBIC",
        "Appeals and Revision", "Requires 10% pre-deposit of the disputed tax amount to stay recovery",
        "Condonation of delay is capped at 1 month after the 3-month window, provided there is sufficient cause.", "Section 108 to 112",
        "Legislative Enactment", "In force", "https://www.cbic.gov.in/", "CGST Act, 2017", "Active"
    ]
]

# Write out the new files
with open('c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\bns_detailed.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(bns_rows)

with open('c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\bnss_detailed.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(bnss_rows)

with open('c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\bsa_detailed.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(bsa_rows)

with open('c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\income_tax.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(it_rows)

with open('c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\gst.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(gst_rows)

print("Expanded CSV files written successfully.")

# Read the original master file (first 373 rows of master are the baseline)
master_path = 'c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\Indian_Law_and_Supreme_Court_Database_2026_NLPRAG.csv'
temp_master_path = 'c:\\Users\\hp\\Downloads\\BlackCoat-main\\BlackCoat-main\\blackcode-backend\\data\\Indian_Law_and_Supreme_Court_Database_2026_NLPRAG_updated.csv'

with open(master_path, 'r', newline='', encoding='utf-8') as f_in:
    reader = csv.reader(f_in)
    rows = list(reader)

header = rows[0]
existing_data = []

# Filter out previously added rows to keep the original baseline clean and prevent duplication
for r in rows[1:]:
    pid = r[0]
    if pid.startswith(('BNS-', 'BNSS-', 'BSA-', 'IT-', 'GST-')):
        continue
    existing_data.append(r)

all_new_rows = bns_rows + bnss_rows + bsa_rows + it_rows + gst_rows

# Verify column counts match
for i, r in enumerate(all_new_rows):
    if len(r) != len(header):
        print(f"Error: Row {i} has length {len(r)}, expected {len(header)}: {r[0]}")

# Append and save
with open(temp_master_path, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(header)
    writer.writerows(existing_data)
    writer.writerows(all_new_rows)

# Overwrite original
os.replace(temp_master_path, master_path)
print(f"Master database CSV updated successfully. Total records: {len(existing_data) + len(all_new_rows) + 1}")
