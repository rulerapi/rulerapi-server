from openapi_server import db


def get_rules():  # noqa: E501
    """get_rules

    Returns the list of rules. # noqa: E501


    :rtype: List[str]
    """
    with db.Session() as session:
        query_result = session.query(db.RulesDB).all()
    rules = []
    for result in query_result:
        rules.append(result.rule_id)
    return rules
