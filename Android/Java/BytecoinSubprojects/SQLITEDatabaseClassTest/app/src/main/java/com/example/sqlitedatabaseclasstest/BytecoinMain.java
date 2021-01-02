package com.example.sqlitedatabaseclasstest;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.widget.TextView;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;


public class BytecoinMain{

    private SQLiteDatabase conn;
    public DatabaseQueries databaseQueries;

    BytecoinMain(SQLiteDatabase connection, TextView textView){
        this.conn = connection;
        textView.setText("connected");

        this.databaseQueries = new DatabaseQueries(this.conn);
    }

    public void closeConnection(){
        this.conn.close();
        this.databaseQueries.closeQueryConnection();
    }

    public static class DatabaseQueries {

        private SQLiteDatabase conn;
        public UserQueries userQueries;

        DatabaseQueries(SQLiteDatabase con){
            this.conn = con;
            userQueries = new UserQueries(this.conn);
        }

        public void createTables(){
            this.conn.execSQL("CREATE TABLE IF NOT EXISTS USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)");
            this.conn.execSQL("CREATE TABLE IF NOT EXISTS WALLETS (id_wallet INTEGER PRIMARY KEY, id_user INTEGER NOT NULL REFERENCES USERS(id_user), bytecoin REAL NOT NULL)");
            this.conn.execSQL("CREATE TABLE IF NOT EXISTS LOGS (sender_wallet INTEGER NOT NULL, receiver_wallet NOT NULL, transaction_date TEXT NOT NULL)");
        }

        public void closeQueryConnection(){
            this.conn.close();
        }


        public String getMD5(String input) {
            try{
                MessageDigest md = MessageDigest.getInstance("MD5");
                byte[] messageDigest = md.digest(input.getBytes());
                BigInteger number = new BigInteger(1, messageDigest);
                String hashtext = number.toString(16);
                while (hashtext.length() < 32){hashtext = "0" + hashtext;}
                return hashtext;}
            catch (NoSuchAlgorithmException e){throw new RuntimeException(e);}
        }

        public int getTableLen(String table_name){
            Cursor cursor = this.conn.rawQuery("SELECT COUNT(*) FROM "+table_name+"",null);
            cursor.moveToFirst();
            return Integer.parseInt(cursor.getString(0));
        }
    }

    public static class UserQueries extends DatabaseQueries{
        private SQLiteDatabase conn;

        UserQueries(SQLiteDatabase con) {
            super(con);
            this.conn = con;
        }

        public void insertUser(String username, String password){
            if(this.getTableLen("USERS") < 1 && this.getTableLen("WALLETS") < 1){
                this.conn.execSQL("INSERT INTO USERS (username, password) VALUES ('"+username+"', '"+getMD5(password)+"')");
                this.conn.execSQL("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES (10001, 1, 0)");
            }else{
                int lastId, lastWalletId;
                Cursor cursor = this.conn.rawQuery("SELECT id_user FROM WALLETS;", null);
                cursor.moveToLast();
                lastId = Integer.parseInt(cursor.getString(0));
                cursor = this.conn.rawQuery("SELECT id_wallet FROM WALLETS;", null);
                cursor.moveToLast();
                lastWalletId = Integer.parseInt(cursor.getString(0));

                lastId+=1;
                lastWalletId+=1;

                this.conn.execSQL("INSERT INTO USERS (username, password) VALUES ('"+username+"', '"+getMD5(password)+"')");
                this.conn.execSQL("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES ("+lastWalletId+", "+lastId+", 0)");
            }
        }
    }
}

