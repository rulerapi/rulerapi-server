from openapi_server import db


def get_rule(rule_id):  # noqa: E501
    """get_rule

    Returns the content of a rule. # noqa: E501

    :param rule_id: Rule ID to get
    :type rule_id: str

    :rtype: str
    """
    with db.Session() as session:
        query_result = session.query(db.RulesDB).filter_by(rule_id=rule_id).one_or_none()
        if query_result is not None:
            return query_result
        else:
            return f"Rule {rule_id} does not exist!"
