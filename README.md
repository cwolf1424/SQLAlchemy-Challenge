# SQLAlchemy-challenge
Challenge assignment for SQLAlchemy

Data for this challenge was from the provided challenge files.

Layout for assignment came from starter file.

Specific sections using sources listed below:

--------------------------------------------------
Setup
--------------------------------------------------

Dependency imports provided in starter file.

--------------------------------------------------
Exploratory Precipitation Analysis
--------------------------------------------------

The following section:

    # Find columns in table
    columns=inspector.get_columns('measurement')
    for c in columns:
        print (c["name"],c["type"])

Used the code provided in week 10, day 3 activity 02-Ins_Dates


The following section:

    mm_latest_date = session.query(measurements.date).order_by(measurements.date.desc()).first()

Used format provided in week 10, day 3, activity 02-Ins_Dates:

    session.query(Dow.date).order_by(Dow.date.desc()).first()

