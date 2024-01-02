import requests
import json
UNDEFINED = "UNDEFINED"
UNDEFINED_INT = 0
UNDEFINED_BOOLEAN = False

def get_request(url):
    resp = requests.get(url)
    return resp.text

def add_to_comments(text, commentCollector):
    json_infos = json.loads(text)
    for json_info in json_infos:
        # populate overall db
        comment = commentCollector.comment.add()

        # user information
        assert "user" in json_info, print("error, user not a valid key here")
        _user = comment.user
        _user.login = json_info["user"].get("login", UNDEFINED)
        _user.id = json_info["user"].get("id", UNDEFINED)
        _user.node_id = json_info["user"].get("node_id", UNDEFINED)
        _user.avatar_url = json_info["user"].get("avatar_url", UNDEFINED)
        _user.gravatar_id = json_info["user"].get("gravatar_id", UNDEFINED)
        _user.url = json_info["user"].get("url", UNDEFINED)
        _user.html_url = json_info["user"].get("html_url", UNDEFINED)
        _user.followers_url = json_info["user"].get("followers_url", UNDEFINED)
        _user.following_url = json_info["user"].get("following_url", UNDEFINED)
        _user.gists_url = json_info["user"].get("gists_url", UNDEFINED)
        _user.starred_url = json_info["user"].get("starred_url", UNDEFINED)
        _user.subscriptions_url = json_info["user"].get("subscriptions_url", UNDEFINED)
        _user.organizations_url = json_info["user"].get("organizations_url", UNDEFINED)
        _user.repos_url = json_info["user"].get("repos_url", UNDEFINED)
        _user.events_url = json_info["user"].get("events_url", UNDEFINED)
        _user.received_events_url = json_info["user"].get("received_events_url", UNDEFINED)
        _user.type = json_info["user"].get("type", UNDEFINED)
        _user.site_admin = json_info["user"].get("site_admin", UNDEFINED)

        # reactions information (note that the default value of ints are 0.)
        assert "reactions" in json_info, print("error, reactions not a valid key here")
        _reactions = comment.reactions
        _reactions.url = json_info["reactions"].get("url", UNDEFINED)
        _reactions.total_count = json_info["reactions"].get("total_count", UNDEFINED_INT)
        _reactions.plus_one = int(json_info["reactions"].get("+1", UNDEFINED_INT))
        _reactions.minus_one = int(json_info["reactions"].get("-1", UNDEFINED_INT))
        _reactions.laugh = int(json_info["reactions"].get("laugh", UNDEFINED_INT))
        _reactions.hooray = int(json_info["reactions"].get("hooray", UNDEFINED_INT))
        _reactions.confused = int(json_info["reactions"].get("confused", UNDEFINED_INT))
        _reactions.heart = int(json_info["reactions"].get("heart", UNDEFINED_INT))
        _reactions.rocket = int(json_info["reactions"].get("rocket", UNDEFINED_INT))
        _reactions.eyes = int(json_info["reactions"].get("eyes", UNDEFINED_INT))


        # comment information
        comment.url = json_info.get("url", UNDEFINED)
        comment.html_url = json_info.get("html_url", UNDEFINED)
        comment.issue_url = json_info.get("issue_url", UNDEFINED)
        comment.id = json_info.get("id", UNDEFINED)
        comment.node_id = json_info.get("node_id", UNDEFINED)
        comment.created_at = json_info.get("created_at", UNDEFINED)
        comment.updated_at = json_info.get("updated_at", UNDEFINED)
        comment.author_association = json_info.get("author_association", UNDEFINED)
        comment.body = json_info.get("body", UNDEFINED)


def add_to_collection(text, respCollector):
    json_info = json.loads(text)
    
    # populate overall db
    response = respCollector.response.add()
    
    # user information
    assert "user" in json_info, print("error, user not a valid key here")
    _user = response.user
    _user.login = json_info["user"].get("login", UNDEFINED)
    _user.id = json_info["user"].get("id", UNDEFINED)
    _user.node_id = json_info["user"].get("node_id", UNDEFINED)
    _user.avatar_url = json_info["user"].get("avatar_url", UNDEFINED)
    _user.gravatar_id = json_info["user"].get("gravatar_id", UNDEFINED)
    _user.url = json_info["user"].get("url", UNDEFINED)
    _user.html_url = json_info["user"].get("html_url", UNDEFINED)
    _user.followers_url = json_info["user"].get("followers_url", UNDEFINED)
    _user.following_url = json_info["user"].get("following_url", UNDEFINED)
    _user.gists_url = json_info["user"].get("gists_url", UNDEFINED)
    _user.starred_url = json_info["user"].get("starred_url", UNDEFINED)
    _user.subscriptions_url = json_info["user"].get("subscriptions_url", UNDEFINED)
    _user.organizations_url = json_info["user"].get("organizations_url", UNDEFINED)
    _user.repos_url = json_info["user"].get("repos_url", UNDEFINED)
    _user.events_url = json_info["user"].get("events_url", UNDEFINED)
    _user.received_events_url = json_info["user"].get("received_events_url", UNDEFINED)
    _user.type = json_info["user"].get("type", UNDEFINED)
    _user.site_admin = json_info["user"].get("site_admin", UNDEFINED)
    
    # closed by information
    assert "closed_by" in json_info, print("error, closed_by not a valid key here")
    if json_info["closed_by"]:
        _closed_by = response.closed_by
        _closed_by.login = json_info["closed_by"].get("login", UNDEFINED)
        _closed_by.id = json_info["closed_by"].get("id", UNDEFINED)
        _closed_by.node_id = json_info["closed_by"].get("node_id", UNDEFINED)
        _closed_by.avatar_url = json_info["closed_by"].get("avatar_url", UNDEFINED)
        _closed_by.gravatar_id = json_info["closed_by"].get("gravatar_id", UNDEFINED)
        _closed_by.url = json_info["closed_by"].get("url", UNDEFINED)
        _closed_by.html_url = json_info["closed_by"].get("html_url", UNDEFINED)
        _closed_by.followers_url = json_info["closed_by"].get("followers_url", UNDEFINED)
        _closed_by.following_url = json_info["closed_by"].get("following_url", UNDEFINED)
        _closed_by.gists_url = json_info["closed_by"].get("gists_url", UNDEFINED)
        _closed_by.starred_url = json_info["closed_by"].get("starred_url", UNDEFINED)
        _closed_by.subscriptions_url = json_info["closed_by"].get("subscriptions_url", UNDEFINED)
        _closed_by.organizations_url = json_info["closed_by"].get("organizations_url", UNDEFINED)
        _closed_by.repos_url = json_info["closed_by"].get("repos_url", UNDEFINED)
        _closed_by.events_url = json_info["closed_by"].get("events_url", UNDEFINED)
        _closed_by.received_events_url = json_info["closed_by"].get("received_events_url", UNDEFINED)
        _closed_by.type = json_info["closed_by"].get("type", UNDEFINED)
        _closed_by.site_admin = json_info["closed_by"].get("site_admin", UNDEFINED)
    
    # reactions information (note that the default value of ints are 0.)
    assert "reactions" in json_info, print("error, reactions not a valid key here")
    _reactions = response.reactions
    _reactions.url = json_info["reactions"].get("url", UNDEFINED)
    _reactions.total_count = json_info["reactions"].get("total_count", UNDEFINED_INT)
    _reactions.plus_one = int(json_info["reactions"].get("+1", UNDEFINED_INT))
    _reactions.minus_one = int(json_info["reactions"].get("-1", UNDEFINED_INT))
    _reactions.laugh = int(json_info["reactions"].get("laugh", UNDEFINED_INT))
    _reactions.hooray = int(json_info["reactions"].get("hooray", UNDEFINED_INT))
    _reactions.confused = int(json_info["reactions"].get("confused", UNDEFINED_INT))
    _reactions.heart = int(json_info["reactions"].get("heart", UNDEFINED_INT))
    _reactions.rocket = int(json_info["reactions"].get("rocket", UNDEFINED_INT))
    _reactions.eyes = int(json_info["reactions"].get("eyes", UNDEFINED_INT))

    # response information 
    # Not implemented: labels, assignees, ClosedBy, milestone, active_lock_reason
    response.url = json_info.get("url", UNDEFINED)
    response.repository_url = json_info.get("repository_url", UNDEFINED)
    response.labels_url = json_info.get("labels_url", UNDEFINED)
    response.comments_url = json_info.get("comments_url", UNDEFINED)
    response.events_url = json_info.get("events_url", UNDEFINED)
    response.html_url = json_info.get("html_url", UNDEFINED)
    response.id = json_info.get("id", UNDEFINED_INT)
    response.node_id = json_info.get("node_id", UNDEFINED)
    response.number = json_info.get("number", UNDEFINED_INT)
    response.title = json_info.get("title", UNDEFINED)
    response.state = json_info.get("state", UNDEFINED)
    response.locked = json_info.get("locked", UNDEFINED_BOOLEAN)
    #response.milestone = json_info.get("milestone", UNDEFINED)
    response.comments = json_info.get("comments", UNDEFINED_INT)
    response.created_at = json_info.get("created_at", UNDEFINED)
    response.updated_at = json_info.get("updated_at", UNDEFINED)
    response.closed_at = json_info.get("closed_at", UNDEFINED)
    response.author_association = json_info.get("author_association", UNDEFINED)
    #response.active_lock_reason = json_info.get("active_lock_reason", UNDEFINED)
    response.body = json_info.get("body", UNDEFINED)
    response.timeline_url = json_info.get("timeline_url", UNDEFINED)
    #response.performed_via_github_app = json_info.get("performed_via_github_app", UNDEFINED)
    response.state_reason = json_info.get("state_reason", UNDEFINED)