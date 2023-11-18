import sqlite3
# import views.surveys as Qs

connection = sqlite3.Connection("sirdar_survey.db")
cursor = connection.cursor()

enterprise_questions = [
    "There is an up-to-date board charter in place appropriate to the life-stage of the organisation and its current structure.",
    "There is an up-to-date delegation of authority policy in place, which is effectively monitored.",
    "The managing director's report effectively communicates status, identifies issues, and clearly indicates a linkage to the business plan.",
    "Board packs are structured and used effectively to guide the board to make decisions and hold those authorised to make decisions accountable.",
    "The board calendar is up-to-date and relevant for the timing requirements of the enterprise and its strategic focus.",
    "All board meeting dates (and committee dates if applicable) for the year are scheduled in directors' diaries and align with the board calendar.",
    "The organisation has an up-to-date strategy (identifying the company's purpose and medium-term vision) and a business plan (identifying the necessary next steps) that guides its focus and direction.",
    "The board ensures a strategic focus in every board meeting to ensure that board papers relevant to the theme agreed upon for that meeting are prepared and that necessary key strategic issues are addressed proactively.",
    "There is clarity regarding the organisation's culture, values, and beliefs.",
    "The culture and values of the organisation are demonstrated by the board, setting the appropriate tone for the rest of the organisation to follow.",
    "The board's conduct is characterised by trust, respect, candour, professionalism, accountability, diligence and commitment.",
    "The organisation has developed a culture of accountability for performance.",
    "The board committees (where appropriate) have approved terms of reference.",
    "The board committees (where appropriate) have an agreed work plan for the year and are making good progress against that plan."
]

Accountability_questions = [
            "The chairman and managing director meet before every board meeting, and this engagement delivers value to the board's focus and preparation, as well as enhancing the relationship between the board and management.",
            "Independent directors meet before every board meeting and utilise this engagement to focus on value creation and enhance effective governance implementation.",
            "The board is effective at passing resolutions based on thorough discussions and the information presented in board papers.",
            "Shareholder-managers demonstrate their acceptance of the authority of the board.",
            "There is a succession plan in place for the chief executive and this plan is proceeding as designed.",
            "The chief executive/managing director has KPIs (Key Performance Indicators) in place and is held accountable for their performance against these indicators.",
            "Board papers are distributed to the board at least seven working days prior to each board meeting.",
            "An updated performance or measurement dashboard is provided in every set of board papers.",
            "The measurement dashboard is used effectively and enables to board to predict the likely future performance of the organisation.",
            "The chief executive/managing director's report is well-designed to be substantially comprehensive and provide an accurate reflection of the performance of the organisation. ",
            "Every board meeting takes place.",
            "Directors attend every scheduled board meeting.",
            "All directors of the board are prompt at reviewing circulated minutes and providing feedback, ideally within two working days. ",
            "Directors are rotated every three years or as per the board charter."
        ]

sustainability_questions = [
            "All relevant and strategic (material) internal and external stakeholders have been identified",
            "Stakeholder requirements (needs, interests, and expectations) are regularly assessed and understood to ensure the delivery of long-term, sustainable benefits.",
            "There is a strategic approach to stakeholder engagement that ensures that the board and the rest of the organisation engage with stakeholders appropriately.",
            "The organisation holds an annual general meeting every year.",
            "The annual general meeting is effective at formally engaging shareholders.",
            "The expectations of shareholders are understood, including both financial and non-financial outcomes, and the board manages these expectations so that they are more realistic where necessary.",
            "The value that the organisation seeks is sustainable over time and meets the needs and expectations of shareholders, stakeholders and interested parties alike.",
            "The audited annual financial statements are available for the previous year-end.",
            "The board has determined the organisation's risk appetite and tolerance levels across all dimensions of the organisation's operations and performance.",
            "A risk framework has been defined and implemented in line with this risk appetite and tolerance.",
            "This risk framework facilitates the regular examination of both the internal operations of the organisation and the external environment to identify risks and implement mitigation strategies",
            "All risks are managed appropriately in line with the risk management framework.",
            "The organisation acts in a socially responsible manner and delivers on its CSR (Community Social Responsibility) plan.",
            "The organisation operates in an environmentally sustainable manner and reports on its environmental impact."
        ]

conformance_questions = [
            "Directors understand the contents of the organisation’s incorporation and founding documents (organisation constitution or memorandum of incorporation or other such documents).",
            "The appointed directors have been duly registered as directors of the organisation with the relevant companies' commission.",
            "Each board director maintains an up-to-date conflict of interest register.",
            "The organisation’s directors’ and officers’ liability insurance is current and sufficient.",
            "There is a regular policy review process that enables the board to recieves, review and approves both new and updated organisation policies on a regular basis.",
            "The board, and each individual director, understand the financial model, activities and performance of the organisation.",
            "The monthly financial measures that are tracked are up-to-date and actively monitored.",
            "The financial report includes an income statement, balance sheet, cash flow forecast and financial ratios.",
            "The monthly financial reports indicate that profitability, business value and solvency are improving.",
            "The organisation has met solvency requirements.",
            "The executive team has the necessary financial understanding and competence, supported by a finance manager, chief financial officer or outsourced provide who leads this element of the organisation's management.",
            "An objective and regular operational assessment is actively used to monitor and evaluate organisation performance and focus ongoing improvement activity within the organisation.",
            "An objective and regular governance assessment or evaluation is actively used by the board to monitor its own performance and cultivate a culture of continuous improvement of the board.",
            "Directors regularly attend director training and continuous professional development, and demonstrate their commitment to continuous learning."
        ]


def carryout_query(statement: str, values: tuple):
    '''calls the execute method, commits and the closes the connection'''

    cursor.execute(statement,values)
    connection.commit()


def quit_connection():
    '''closes the connection to the database and cleans up resources'''

    cursor.close()
    connection.close()


def add_respondent(company_name, position):
    '''adds a new board member to the respondents table'''

    insert = "INSERT INTO Respondents (CompanyName, Position) VALUES ('?', '?');"
    values = (company_name, position)
    carryout_query(insert, values)


def add_categories():
    '''adds a new board member to the respondents table'''

    insert = """INSERT INTO Categories (CategoryID, CategoryName)
                VALUES (1, 'Enterprise Purpose'),
                    (2, 'Accountability for Performance'),
                    (3, 'Sustainability'),
                    (4, 'Conformance');"""
    cursor.execute(insert)
    connection.commit()


def add_enterprise_questions():
    '''adds a new board member to the respondents table'''
    # questions: list[str] = Qs.enterprise_questions

    for i in range(len(enterprise_questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 1, ?);"""
        values = (i+1, enterprise_questions[i])
        carryout_query(insert, values)


def add_performance_questions():
    '''adds a new board member to the respondents table'''
    # questions: list[str] = Qs.Accountability_questions
    
    count = 15
    for i in range(len(Accountability_questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 2, ?);"""
        values = (count, Accountability_questions[i])
        count += 1
        carryout_query(insert, values)


def add_sustainability_questions():
    '''adds a new board member to the respondents table'''

    # questions: list[str] = Qs.sustainability_questions

    count = 29
    for i in range(len(sustainability_questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 3, ?);"""
        values = (count, sustainability_questions[i])
        count += 1
        carryout_query(insert, values)


def add_conformance_questions():
    '''adds a new board member to the respondents table'''
    # questions: list[str] = Qs.conformance_questions
    count = 43
    for i in range(len(conformance_questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 4, ?);"""
        values = (count, conformance_questions[i])
        count += 1
        carryout_query(insert, values)


def add_response(respondent_id: int, question_id: int, response: str):
    '''adds a new board member to the respondents table'''

    insert = "INSERT INTO Responses (RespondentID, QuestionID, Response) VALUES (?, ?, ?);"
    values = (respondent_id, question_id, response)
    carryout_query(insert, values)

add_conformance_questions()

print("SUCCESS")