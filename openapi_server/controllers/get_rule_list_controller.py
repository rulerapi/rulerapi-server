from openapi_server import db


def get_rules(ruleset):  # noqa: E501
    """get_rules

    Returns the list of rules. # noqa: E501


    :rtype: List[str]
    """
    with db.Session() as session:
        query_result = session.query(db.RulesDB).filter_by(ruleset=ruleset)
    rules = []
    for result in query_result:
        rules.append(result.rule_id)
    return rules
