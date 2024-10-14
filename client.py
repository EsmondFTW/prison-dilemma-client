import asyncio
import websockets
import json

async def play_rounds(websocket, player_id, rounds, initial_move):
    opponent_prev_move = None
    for _ in range(rounds):
        if opponent_prev_move is None:
            # First move, send the initial move
            move_data = json.dumps({"player_id": player_id, "move": initial_move})

        # Your logic starts here
        else:
            # Subsequent moves, use a simple tit-for-tat strategy
            if opponent_prev_move == "C":
                move = "C"  # Cooperate if opponent cooperated
            else:
                move = "D"  # Defect if opponent defected
            move_data = json.dumps({"player_id": player_id, "move": move})

        # Your logic ends here

        await websocket.send(move_data)
        result = await websocket.recv()
        result_data = json.loads(result)
        print(f"Player {player_id} result: {result_data['result']} move made by other player {result_data['move']}")
        

        # Update opponent's previous move
        opponent_prev_move = result_data['move']

async def play_game(player_id, move):
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send(player_id)
        rounds = int(await websocket.recv())  # Convert rounds to int
        print(rounds)

        await play_rounds(websocket, player_id, rounds, move)

# Run the client
asyncio.run(play_game("Team1", "C")) #args team_id, first move
