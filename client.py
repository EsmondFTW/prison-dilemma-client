import asyncio
import websockets
import json
from strategy import strategy  # Import the strategy function

async def play_rounds(websocket, player_id, rounds):
    opponent_prev_move = None
    for _ in range(rounds):
        move = strategy(opponent_prev_move)
        
        move_data = json.dumps({"player_id": player_id, "move": move})
        await websocket.send(move_data)
        result = await websocket.recv()
        result_data = json.loads(result)
        print(f"Player {player_id} result: {result_data['result']} move made by other player {result_data['move']}")
        
        # Update opponent's previous move
        opponent_prev_move = result_data['move']

async def play_game(player_id):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(player_id)
        rounds = int(await websocket.recv())  # Convert rounds to int
        print(rounds)

        await play_rounds(websocket, player_id, rounds)

# Run the client
asyncio.run(play_game("Team_4"))  # args team_id, first move