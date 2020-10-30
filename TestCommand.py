import random


async def standard_roll(ctx, roll: str):
    """Rolls a dice using #d# format.
    e.g /r 3d6"""

    result_total = 0
    result_string = ''
    try:
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
            "Rolling %s d%s for %s" % (num_dice, dice_val, ctx.message.author.name))
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
