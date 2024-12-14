import random as r
import string, asyncio

def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(pass_length):
        password += r.choice(elements)
    return password

async def handle_guess(bot, message):
    if message.content.startswith('$guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = r.randint(1, 10)

        try:
            guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')