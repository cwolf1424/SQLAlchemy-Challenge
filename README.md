# SQLAlchemy-challenge
Challenge assignment for SQLAlchemy

Data for this challenge was from the provided challenge files.

Layout for assignment came from starter file.

Specific sections using sources listed below:

--------------------------------------------------
Setup (Climate_Analysis)
--------------------------------------------------

Dependency imports provided in starter file.

--------------------------------------------------
Exploratory Precipitation Analysis (Climate_Analysis)
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

--------------------------------------------------
Exploratory Station Analysis (Climate_Analysis)
--------------------------------------------------

The following section:

    stations_activity = session.query(measurements.station, func.count(measurements.station)).group_by(measurements.station).order_by(func.count(measurements.station).desc()).all()


Used format explained by Liang from the AskBCS team:

    .query(col, func.count(col)).group_by(col)


The following section:

    USC00519281_latest_date = session.query(measurements.date).filter_by(station = 'USC00519281').order_by(measurements.date.desc()).first()

Used format provided in week 10, day 3, activity 02-Ins_Dates:

    session.query(Dow.date).order_by(Dow.date.desc()).first()



--------------------------------------------------
App.py
--------------------------------------------------

In setup, much of the code from the first part of the assignment was re-used.

This section also used code provided in climate_starter file:

    # Python SQL toolkit and Object Relational Mapper
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect

