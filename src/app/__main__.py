from flask import Flask, render_template
import random
from .app import myfunc

def main():
    myfunc()

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        t_warm_base = random.uniform(100.0, 400.0)
        t_cold_chuck = random.uniform(100.0, 400.0)
        t_gripper_bb = random.uniform(100.0, 400.0)
        t_braid_shield = '...'
        print(f'temperatures: {t_warm_base} {t_cold_chuck} {t_cold_chuck} {t_gripper_bb} {t_braid_shield}')
        return render_template("crowconDevice.html", t_warm_base=t_warm_base, t_cold_chuck=t_cold_chuck,
                               t_gripper_bb=t_gripper_bb, t_braid_shield=t_braid_shield)
    
    app.run()


if __name__=="__main__":
    main()
