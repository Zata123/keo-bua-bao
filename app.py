from flask import Flask, render_template, request, session
from random import choice

app = Flask(__name__)

# Dùng để Flask lưu điểm số
app.secret_key = "keo-bua-bao-secret-key"


@app.route("/", methods=["GET", "POST"])
def home():

    # Khởi tạo điểm
    if "user_score" not in session:
        session["user_score"] = 0

    if "computer_score" not in session:
        session["computer_score"] = 0

    player = ""
    computer = ""
    result = "Lượt bạn."

    # Khi người chơi chọn
    if request.method == "POST":

        player = request.form["choice"]

        # Máy chọn ngẫu nhiên
        computer = choice(["kéo", "búa", "bao"])

        # Kiểm tra kết quả
        if player == computer:

            result = "Hòa 🤝"

        elif (
            (player == "kéo" and computer == "bao")
            or
            (player == "búa" and computer == "kéo")
            or
            (player == "bao" and computer == "búa")
        ):

            result = "Bạn thắng! 🎉"
            session["user_score"] += 1

        else:

            result = "Bạn thua! 😭"
            session["computer_score"] += 1

    return render_template(
        "index.html",
        player=player,
        computer=computer,
        result=result,
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )


if __name__ == "__main__":
    app.run()
