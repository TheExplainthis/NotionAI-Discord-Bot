from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_name(cls):
        return list(map(lambda c: c.name, cls))


class TopicEnum(ExtendedEnum):
    brainstorm_ideas = "brainstormIdeas"
    blog_post = "blogPost"
    outline = "outline"
    social_media_post = "socialMediaPost"
    press_release = "pressRelease"
    creative_story = "creativeStory"
    essay = "essay"
    poem = "poem"
    meeting_agenda = "meetingAgenda"
    pros_cons_list = "prosConsList"
    job_description = "jobDescription"
    sales_email = "salesEmail"
    recruiting_email = "recruitingEmail"


class TranslateLanguageEnum(ExtendedEnum):
    english = "English"
    korean = "Korean"
    chinese = "Chinese"
    japanese = "Japanese"
    spanish = "Spanish"
    russian = "Russian"
    french = "French"
    german = "German"
    italian = "Italian"
    portuguese = "Portuguese"
    dutch = "Dutch"
    indonesia = "Indonesian"
    tagalog = "Tagalog"
    vietnamese = "Vietnamese"


class PromptTypeEnum(ExtendedEnum):
    help_me_write = "helpMeWrite"
    continue_writing = "continueWriting"
    change_tone = "changeTone"
    summarize = "summarize"
    improve_writing = "improveWriting"
    fix_spelling_grammar = "fixSpellingGrammar"
    translate = "translate"
    explain_this = "explainThis"
    make_longer = "makeLonger"
    make_shorter = "makeShorter"
    find_action_items = "findActionItems"
    simplify_language = "simplifyLanguage"
    help_me_edit = "helpMeEdit"


class ToneEnum(ExtendedEnum):
    professional = "Professional"
    casual = "Casual"
    straight_forward = "Straightforward"
    confident = "Confident"
    friendly = "Friendly"