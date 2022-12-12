from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)  



@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       low_bound = int(request.form.get("lowyear"))
       upper_bound = int(request.form.get("upperyear"))
       liked_labels = request.form.getlist('movie')
       df0 = pd.read_csv('zero_films.csv')
       df1 = pd.read_csv('one_films.csv')
       df2 = pd.read_csv('two_films.csv')
       df3 = pd.read_csv('three_films.csv')
       df4 = pd.read_csv('fours_films.csv')
       df5 = pd.read_csv('fives_films.csv')
       df6 = pd.read_csv('sixes_films.csv')
       df7 = pd.read_csv('sevens_films.csv')
       df8 = pd.read_csv('eights_films.csv')
       labels =  [df0,df1,df2,df3,df4,df5,df6,df7,df8]
       movies_recommended = []
 
       for label in liked_labels:
         index = int(label)
         relevant_df = labels[index]
         rslt_df1 = relevant_df[relevant_df['year'] > low_bound]
         rslt_df = rslt_df1[rslt_df1['year'] < upper_bound]
         rslt_df.sort_values(by = ['avg_vote', 'total_votes'], ascending = False, inplace = True)
         for i in range(3):
            movies_recommended.append(list(rslt_df['title'])[i])
       return str(movies_recommended)
    return render_template("form.html")

if __name__=='__main__':
   app.run(host = '0.0.0.0', port = 81)