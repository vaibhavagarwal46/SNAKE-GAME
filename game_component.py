import streamlit.components.v1 as components

def snake_game_component():
    html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background: transparent;
            font-family: 'Inter', sans-serif;
        }
        #game-container {
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            border-radius: 20px;
            overflow: hidden;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        canvas {
            display: block;
            background: #1a1a2e;
        }
        #score-board {
            position: absolute;
            top: 20px;
            left: 20px;
            color: #fff;
            font-size: 24px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }
        #game-over {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #fff;
            text-align: center;
            display: none;
            background: rgba(0, 0, 0, 0.8);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid #ff4b2b;
            animation: fadeIn 0.5s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translate(-50%, -60%); }
            to { opacity: 1; transform: translate(-50%, -50%); }
        }
        #game-over h2 {
            margin: 0 0 10px 0;
            font-size: 48px;
            color: #ff4b2b;
        }
        #game-over p {
            font-size: 20px;
            margin-bottom: 20px;
        }
        #restart-btn {
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            border: none;
            color: white;
            padding: 12px 30px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        #restart-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255, 75, 43, 0.4);
        }
    </style>
</head>
<body>
    <div id="game-container">
        <div id="score-board">Score: 0</div>
        <canvas id="gameCanvas" width="600" height="400"></canvas>
        <div id="game-over">
            <h2>GAME OVER</h2>
            <p id="final-score">Your Score: 0</p>
            <button id="restart-btn" onclick="resetGame()">Try Again</button>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreElement = document.getElementById('score-board');
        const gameOverElement = document.getElementById('game-over');
        const finalScoreElement = document.getElementById('final-score');

        const gridSize = 20;
        const tileCountX = canvas.width / gridSize;
        const tileCountY = canvas.height / gridSize;

        let score = 0;
        let dx = 0;
        let dy = 0;
        let snake = [
            {x: 10, y: 10}
        ];
        let food = {x: 5, y: 5};
        let gameActive = true;
        let nextDx = 0;
        let nextDy = 0;

        function drawGame() {
            if (!gameActive) return;

            updateDirection();
            moveSnake();
            
            if (checkGameOver()) {
                endGame();
                return;
            }

            checkFoodCollision();
            clearCanvas();
            drawFood();
            drawSnake();
            
            setTimeout(drawGame, 100);
        }

        function clearCanvas() {
            ctx.fillStyle = '#1a1a2e';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
            ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=gridSize) {
                ctx.beginPath();ctx.moveTo(i,0);ctx.lineTo(i,canvas.height);ctx.stroke();
            }
            for(let i=0; i<canvas.height; i+=gridSize) {
                ctx.beginPath();ctx.moveTo(0,i);ctx.lineTo(canvas.width,i);ctx.stroke();
            }
        }

        function drawSnake() {
            snake.forEach((part, index) => {
                const alpha = 1 - (index / snake.length) * 0.6;
                ctx.fillStyle = index === 0 ? '#00f2fe' : `rgba(79, 172, 254, ${alpha})`;
                
                const r = index === 0 ? 8 : 4;
                fillRoundRect(ctx, part.x * gridSize + 2, part.y * gridSize + 2, gridSize - 4, gridSize - 4, r);
            });
        }

        function fillRoundRect(ctx, x, y, width, height, radius) {
            ctx.beginPath();
            ctx.moveTo(x + radius, y);
            ctx.lineTo(x + width - radius, y);
            ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
            ctx.lineTo(x + width, y + height - radius);
            ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
            ctx.lineTo(x + radius, y + height);
            ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
            ctx.lineTo(x, y + radius);
            ctx.quadraticCurveTo(x, y, x + radius, y);
            ctx.closePath();
            ctx.fill();
        }

        function drawFood() {
            ctx.fillStyle = '#ff4b2b';
            ctx.shadowBlur = 15;
            ctx.shadowColor = '#ff4b2b';
            ctx.beginPath();
            ctx.arc(food.x * gridSize + gridSize/2, food.y * gridSize + gridSize/2, gridSize/2 - 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;
        }

        function moveSnake() {
            dx = nextDx;
            dy = nextDy;
            
            if (dx === 0 && dy === 0) return;

            const head = {x: snake[0].x + dx, y: snake[0].y + dy};
            
            if (head.x < 0) head.x = tileCountX - 1;
            if (head.x >= tileCountX) head.x = 0;
            if (head.y < 0) head.y = tileCountY - 1;
            if (head.y >= tileCountY) head.y = 0;

            snake.unshift(head);
            snake.pop();
        }

        function updateDirection() {
        }

        function checkFoodCollision() {
            if (snake[0].x === food.x && snake[0].y === food.y) {
                score += 10;
                scoreElement.innerHTML = `Score: ${score}`;
                snake.push({...snake[snake.length-1]});
                generateFood();
            }
        }

        function generateFood() {
            food = {
                x: Math.floor(Math.random() * tileCountX),
                y: Math.floor(Math.random() * tileCountY)
            };
            if (snake.some(part => part.x === food.x && part.y === food.y)) {
                generateFood();
            }
        }

        function checkGameOver() {
            if (dx === 0 && dy === 0) return false;
            
            const head = snake[0];
            for (let i = 1; i < snake.length; i++) {
                if (snake[i].x === head.x && snake[i].y === head.y) {
                    return true;
                }
            }
            return false;
        }

        function endGame() {
            gameActive = false;
            gameOverElement.style.display = 'block';
            finalScoreElement.innerHTML = `Your Score: ${score}`;
        }

        function resetGame() {
            score = 0;
            dx = 0; dy = 0;
            nextDx = 0; nextDy = 0;
            snake = [{x: 10, y: 10}];
            gameActive = true;
            scoreElement.innerHTML = `Score: 0`;
            gameOverElement.style.display = 'none';
            generateFood();
            drawGame();
        }

        window.addEventListener('keydown', e => {
            switch (e.key) {
                case 'ArrowUp':
                    if (dy !== 1) { nextDx = 0; nextDy = -1; }
                    break;
                case 'ArrowDown':
                    if (dy !== -1) { nextDx = 0; nextDy = 1; }
                    break;
                case 'ArrowLeft':
                    if (dx !== 1) { nextDx = -1; nextDy = 0; }
                    break;
                case 'ArrowRight':
                    if (dx !== -1) { nextDx = 1; nextDy = 0; }
                    break;
            }
            if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
                e.preventDefault();
            }
        });

        generateFood();
        drawGame();
    </script>
</body>
</html>
    """
    components.html(html_code, height=450)
