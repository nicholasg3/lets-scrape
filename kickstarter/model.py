import sqlalchemy as sqla


metadata = sqla.MetaData()

engine = sqla.create_engine('mysql://root@localhost/kickstarter')
conn = engine.connect()


campaign_basics = sqla.Table(
    'campaigns', metadata,
    sqla.Column('user_id', sqla.Integer, primary_key=True),
    sqla.Column('user_name', sqla.String(16), nullable=False),
    sqla.Column('email_address', sqla.String(60), key='email'),
    sqla.Column('password', sqla.String(20), nullable=False)
)
