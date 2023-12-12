from flask import Flask, render_template, session, redirect, url_for,jsonify
import mysql.connector
import json
from decimal import Decimal



class user_model():
    def __init__(self):
            try:
               self.con=mysql.connector.connect(host="localhost",user="root",password="nineleaps",database="IPL")
               self.con.autocommit=True
               self.cur=self.con.cursor(dictionary=True)
               print("Connection Successful")
            except:
                print("Some error")

    def user_getall_model(self):
      self.cur.execute("select * from IPLdata")
      result=self.cur.fetchall()
      if len(result)>0:
             return json.dumps(result)
      else:
            return "NO DATA FOUND"

    def user_addone_model(self, data):
     try:
        self.cur.execute("INSERT INTO Retained(`Player Name`, Team, Price) VALUES (%s, %s, %s)",
                         (data['name'], data['team'], data['price']))
        self.con.commit()
        return "Player added successfully"
     except Exception as e:
        return f"Error adding player: {str(e)}"

    # def user_update_model(self,data):
    #   player_id = data.get('id')
    #   print(f"Updating player with ID: {player_id}")
    #   self.cur.execute(f"UPDATE IPLdata SET Sold = 1 WHERE PlayerID=%s", (player_id,))
    #   if self.cur.rowcount>0:
    #     return "User Updated Successfully"
    #   else:
    #       return "Nothing to update"
      
    def user_getpurse_model(self, data):
      try:
        team_name = data.get('team')
        query = "SELECT COALESCE(10000 - SUM(Price), 10000) AS remaining_purse FROM Retained WHERE Team = %s GROUP BY Team"
        self.cur.execute(query, (team_name,))
        result = self.cur.fetchone()

        if result:
            result['remaining_purse'] = float(result['remaining_purse'])
            return json.dumps(result)
        else:
            return "NO DATA FOUND"
      except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error"
     
    def user_selectedteam_model(self, data):
      try:
        team_name = data.get('team')
        query = "SELECT `Player Name` FROM Retained WHERE Team = %s "
        self.cur.execute(query, (team_name,))
        result = self.cur.fetchall()
        return json.dumps(result)
        
      except Exception as e:
        print(f"Error: {e}")
        return "Internal Server Error"     


    def user_delete_model(self,data):
      player_id = data.get('id')
      self.cur.execute(f"DELETE FROM IPLdata WHERE PlayerID=%d", (player_id,))
      if self.cur.rowcount>0:
        return "User Deleted Successfully"
      else:
          return "Nothing to Delete"          
      
      