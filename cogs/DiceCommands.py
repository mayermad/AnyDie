import discord
from discord.ext import commands
import random
import re


class DiceCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def r(self, ctx, roll: str):
        """Rolls a dice using #d# format.
        e.g /r 3d6"""

        result_total = 0
        result_string = ''
        try:
            await ctx.message.delete()
            try:
                num_dice = roll.split('d')[0]
                dice_val = roll.split('d')[1]
            except Exception as e:
                print(e)
                await ctx.message.channel.send("Format has to be in #d# %s." % ctx.message.author.name)
                return

            if int(num_dice) > 500:
                await ctx.message.channel.send("I cant roll that many dice %s." % ctx.message.author.name)
                return

            # await delete_messages(ctx.message, ctx.message.author)

            await ctx.message.channel.send(
                "Rolling %s d%s for %s" % (num_dice, dice_val, str(ctx.message.author.display_name)))
            rolls, limit = map(int, roll.split('d'))

            for ir in range(rolls):
                number = random.randint(1, limit)
                result_total = result_total + number

                if result_string == '':
                    result_string += str(number)
                else:
                    result_string += ', ' + str(number)

            if num_dice == '1':
                await ctx.message.channel.send(
                    ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string)
            else:
                await ctx.message.channel.send(
                    ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string + "\n**Total:** " + str(
                        result_total))

        except Exception as e:
            print(e)
            return

    @commands.command(pass_context=True)
    async def rt(self, ctx, roll: str):
        """Rolls dice using #d#s# format with a set success threshold, Where s is the threshold type (< = >).
        e.g .r 3d10<55"""

        number_successes = 0
        result_string = ''

        try:
            value_list = re.split("(\d+)", roll)
            value_list = list(filter(None, value_list))

            dice_count = int(value_list[0])
            dice_value = int(value_list[2])
            threshold_sign = value_list[3]
            success_threshold = int(value_list[4])

        except Exception as e:
            print(e)
            await ctx.message.channel.send("Format has to be in #d#t# %s." % ctx.message.author.name)
            return

        if int(dice_count) > 500:
            await ctx.message.channel.send("I cant roll that many dice %s." % ctx.message.author.name)
            return

        # await delete_messages(ctx.message, ctx.message.author)

        await ctx.message.channel.send("Rolling %s d%s for %s with a success threshold %s %s" % (
            dice_count, dice_value, ctx.message.author.name, threshold_sign, success_threshold))

        try:
            for kr in range(0, dice_count):

                number = random.randint(1, dice_value)
                is_roll_success = False

                if threshold_sign == '<':
                    if number < success_threshold:
                        number_successes += 1
                        is_roll_success = True

                elif threshold_sign == '=':
                    if number == success_threshold:
                        number_successes += 1
                        is_roll_success = True

                else:  # >
                    if number > success_threshold:
                        number_successes += 1
                        is_roll_success = True

                if result_string == '':
                    if is_roll_success:
                        result_string += '**' + str(number) + '**'
                    else:
                        result_string += str(number)
                else:
                    if is_roll_success:
                        result_string += ', ' + '**' + str(number) + '**'
                    else:
                        result_string += ', ' + str(number)

            if dice_count == 1:
                if number_successes == 0:
                    await ctx.message.channel.send(
                        ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string + "\n**Success:** :x:")
                else:
                    await ctx.message.channel.send(
                        ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string + "\n**Success:** :white_check_mark:")
            else:
                await ctx.message.channel.send(
                    ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string + "\n**Successes:** " + str(
                        number_successes))
        except Exception as e:
            print(e)
            return

    @commands.command(pass_context=True)
    async def c(self, ctx, roll: str, val):
        """Rolls a dice using #d# format.
        e.g /r 3d6"""

        result_total = 0
        result_string = ''
        try:
            await ctx.message.delete()
            print("cheater")
            try:
                num_dice = roll.split('d')[0]
                dice_val = roll.split('d')[1]
            except Exception as e:
                print(e)
                await ctx.message.channel.send("Format has to be in #d# %s." % ctx.message.author.name)
                return

            if int(num_dice) > 500:
                await ctx.message.channel.send("I cant roll that many dice %s." % ctx.message.author.name)
                return

            # await delete_messages(ctx.message, ctx.message.author)

            await ctx.message.channel.send(
                "Rolling %s d%s for %s" % (num_dice, dice_val, str(ctx.message.author.display_name)))
            rolls, limit = map(int, roll.split('d'))

            for ir in range(rolls):
                number = int(val)
                result_total = result_total + number

                if result_string == '':
                    result_string += str(number)
                else:
                    result_string += ', ' + str(number)

            if num_dice == '1':
                await ctx.message.channel.send(
                    ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string)
            else:
                await ctx.message.channel.send(
                    ctx.message.author.mention + "  :game_die:\n**Result:** " + result_string + "\n**Total:** " + str(
                        result_total))

        except Exception as e:
            print(e)
            return

def setup(bot):
    bot.add_cog(DiceCommandsCog(bot))
