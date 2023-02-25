
import os

from dotenv import load_dotenv
import discord
from notionai import NotionAI, ToneEnum, TranslateLanguageEnum
from src.discordBot import DiscordClient, Sender
from src.logger import logger
from src.server import keep_alive
load_dotenv()


def run():
    client = DiscordClient()
    sender = Sender()
    notion_ai = NotionAI(os.getenv('NOTION_TOKEN'), os.getenv('NOTION_SPACE_ID'))

    @client.tree.command(name="help_me_write", description="Help me write, ask AI to write for you")
    async def help_me_write(interaction: discord.Interaction, *, prompt: str, context: str, page_title: str = "", rest_content: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.help_me_write(prompt, context, page_title, rest_content)
        send_message = f"[help_me_write] prompt: {prompt} \n context: {context} \n page_title: {page_title} \n rest_content: {rest_content}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="continue_write", description="Continue writing, generating more")
    async def continue_write(interaction: discord.Interaction, *, context: str, page_title: str = "", rest_content: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.continue_write(context, page_title, rest_content)
        send_message = f"[continue_write] context: {context} \n page_title: {page_title} \n rest_content: {rest_content}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="help_me_edit", description="Help me edit somethings, it will change the current context")
    async def help_me_edit(interaction: discord.Interaction, *, prompt: str, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.help_me_edit(prompt, context, page_title)
        send_message = f"[help_me_edit] prompt: {prompt} \n context: {context} \n page_title: {page_title} "
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="translate", description="Use NotionAI to translate your context")
    async def translate(interaction: discord.Interaction, *, language: str, context: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        send_message = f"[translate] language: {language} \n context: {context}"

        language = language.lower()
        try:
            language = TranslateLanguageEnum(language)
        except Exception:
            error_message = "❌ Error: The language can only be: english, korean, chinese, japanese, spanish, russiab, french, german, italian, portuguese, dutch, indonesia, tagalog or vietnamese."
            await sender.send_message(interaction, send_message, error_message)
        ai_response = notion_ai.translate(language, context)
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="change_tone", description="Change the tone of your context")
    async def change_tone(interaction: discord.Interaction, *, context: str, tone: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()

        send_message = f"[change_tone] context: {context} \n tone: {tone}"
        try:
            tone = ToneEnum(tone)
        except Exception:
            error_message = "❌ Error: The tone can only be: professional, casual, straightforward, confident, or friendly."
            await sender.send_message(interaction, send_message, error_message)
        ai_response = notion_ai.change_tone(context, ToneEnum(tone))
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="summarize", description="Summarize context")
    async def summarize(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.summarize(context, page_title)
        send_message = f"[summarize] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="improve_writing", description="Improve context")
    async def improve_writing(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.improve_writing(context, page_title)
        send_message = f"[improve_writing] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="fix_spelling_grammar", description="Correcting grammar errors in context")
    async def fix_spelling_grammar(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.fix_spelling_grammar(context, page_title)
        send_message = f"[fix_spelling_grammar] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="explain_this", description="Explanation of Context")
    async def explain_this(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.explain_this(context, page_title)
        send_message = f"[explain_this] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="make_longer", description="Editing text to make the Context longer")
    async def make_longer(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.make_longer(context, page_title)
        send_message = f"[make_longer] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="make_shorter", description="Editing text to make the Context shorter")
    async def make_shorter(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.make_shorter(context, page_title)
        send_message = f"[make_shorter] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="find_action_items", description="Generate action items")
    async def find_action_items(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.find_action_items(context, page_title)
        send_message = f"[find_action_items] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="simplify_language", description="Simplify Context")
    async def simplify_language(interaction: discord.Interaction, *, context: str, page_title: str = ""):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.simplify_language(context, page_title)
        send_message = f"[simplify_language] context: {context} \n page_title: {page_title}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="blog_post", description="Generate post")
    async def blog_post(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.blog_post(prompt)
        send_message = f"[blog_post] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="brainstorm_ideas", description="Generate ideas")
    async def brainstorm_ideas(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.brainstorm_ideas(prompt)
        send_message = f"[brainstorm_ideas] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="outline", description="Generate outline")
    async def outline(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.outline(prompt)
        send_message = f"[outline] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="social_media_post", description="Generate social media post")
    async def social_media_post(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.social_media_post(prompt)
        send_message = f"[social_media_post] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="creative_story", description="Generate creative story")
    async def creative_story(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.creative_story(prompt)
        send_message = f"[creative_story] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="poem", description="Generate poem")
    async def poem(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.poem(prompt)
        send_message = f"[poem] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="essay", description="Generate essay")
    async def essay(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.essay(prompt)
        send_message = f"[essay] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="meeting_agenda", description="Generate meeting agenda")
    async def meeting_agenda(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.meeting_agenda(prompt)
        send_message = f"[meeting_agenda] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="press_release", description="Generate press release")
    async def press_release(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.press_release(prompt)
        send_message = f"[press_release] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="job_description", description="Generate jon description")
    async def job_description(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.job_description(prompt)
        send_message = f"[job_description] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="sales_email", description="Generate sales email")
    async def sales_email(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.sales_email(prompt)
        send_message = f"[sales_email] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="recruiting_email", description="Generate recuiting email")
    async def recruiting_email(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.recruiting_email(prompt)
        send_message = f"[recruiting_email] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    @client.tree.command(name="pros_cons_list", description="Generate prons and cons list")
    async def pros_cons_list(interaction: discord.Interaction, *, prompt: str):
        if interaction.user == client.user:
            return
        await interaction.response.defer()
        ai_response = notion_ai.pros_cons_list(prompt)
        send_message = f"[pros_cons_list] prompt: {prompt}"
        await sender.send_message(interaction, send_message, ai_response)

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    logger.info('Server Run')
    keep_alive()
    run()
