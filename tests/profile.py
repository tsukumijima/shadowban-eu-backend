
import pathlib
import sys
from typing import Any, Tuple, Dict

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from log import log
from util import is_error, is_generic_error, UnexpectedApiError

# Count amount of "possibly_sensitive_editable" and "possibly_sensitive"
# flagged tweets in user's timeline
async def count_sensitives(session, user_id):
   profile_timeline = await session.get_profile_tweets_raw(user_id)
   profile_tweets = profile_timeline["globalObjects"]["tweets"].values()

   counted = len(profile_tweets)
   possibly_sensitive = len([1 for tweet in profile_tweets if "possibly_sensitive" in tweet.keys()])
   possibly_sensitive_editable = len([1 for tweet in profile_tweets if "possibly_sensitive_editable" in tweet.keys()])

   result = {
      "counted": counted,
      "possibly_sensitive": possibly_sensitive,
      "possibly_sensitive_editable": possibly_sensitive_editable
   }

   return result

async def test(session, username: str) -> Tuple[str, Dict[str, Any]]:
    profile: dict[str, Any] = {}
    profile_raw = await session.profile_raw(username)
    log.info('Testing ' + str(username))
    if is_generic_error(profile_raw, [50, 63]):
        log.debug("Other error:" + str(username))
        raise UnexpectedApiError

    try:
        user_id = str(profile_raw["id"])
    except KeyError:
        user_id = ''

    try:
        profile["screen_name"] = profile_raw["screen_name"]
    except KeyError:
        profile["screen_name"] = username

    try:
        if profile_raw["profile_interstitial_type"] != "":
            profile["restriction"] = profile_raw["profile_interstitial_type"]
    except KeyError:
        pass

    try:
        profile["protected"] = profile_raw["protected"]
    except KeyError:
        pass

    profile["exists"] = not is_error(profile_raw, 50)

    suspended = is_error(profile_raw, 63)
    if suspended:
        profile["suspended"] = suspended

    try:
        profile["has_tweets"] = int(profile_raw["statuses_count"]) > 0
    except KeyError:
        profile["has_tweets"] = False


    log.debug(profile)
    if profile["exists"] and not profile.get("protected", False) and not profile.get("suspended", False):
        profile["sensitives"] = await count_sensitives(session, user_id)

    return user_id, profile
