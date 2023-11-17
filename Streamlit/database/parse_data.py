import sqlite3
import views.surveys as Qs

connection = sqlite3.Connection("sirdar_survey.db")
cursor = connection.cursor()


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
    questions: list[str] = Qs.enterprise_questions

    for i in range(len(questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 1, ?);"""
        values = (i+1, questions[i])
        carryout_query(insert, values)


def add_performance_questions():
    '''adds a new board member to the respondents table'''
    questions: list[str] = Qs.Accountability_questions

    for i in range(len(questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 2, ?);"""
        values = (i+1, questions[i])
        carryout_query(insert, values)


def add_sustainability_questions():
    '''adds a new board member to the respondents table'''

    questions: list[str] = Qs.sustainability_questions

    for i in range(len(questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 3, ?);"""
        values = (i+1, questions[i])
        carryout_query(insert, values)


def add_conformance_questions():
    '''adds a new board member to the respondents table'''
    questions: list[str] = Qs.conformance_questions

    for i in range(len(questions)):
        insert = """INSERT INTO Questions (QuestionID, CategoryID, Question)
                    VALUES (?, 4, ?);"""
        values = (i+1, questions[i])
        carryout_query(insert, values)


def add_response(respondent_id: int, question_id: int, response: str):
    '''adds a new board member to the respondents table'''

    insert = "INSERT INTO Responses (RespondentID, QuestionID, Response) VALUES (?, ?, ?);"
    values = (respondent_id, question_id, response)
    carryout_query(insert, values)