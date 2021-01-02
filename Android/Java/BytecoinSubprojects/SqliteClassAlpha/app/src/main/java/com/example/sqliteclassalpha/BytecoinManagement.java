package com.example.sqliteclassalpha;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class BytecoinManagement {

    public static SQLiteDatabase databaseConnection; // SQLITE_DATABASE_CONNECTION

    public DatabaseQueries databaseQueries;
    public UserQueries userQueries;
    public CryptoMethods cryptoMethods;
    public WalletQueries walletQueries;

    BytecoinManagement(SQLiteDatabase connection){
        databaseConnection = connection;

        this.databaseQueries = new DatabaseQueries();
        this.userQueries = new UserQueries();
        this.cryptoMethods = new CryptoMethods();
        this.walletQueries = new WalletQueries();
    }

    public void closeDatabaseConnection(){
        databaseConnection.close();
    }

    public static class DatabaseMethods{
        public static int getTableLen(String table_name){
            Cursor cursor = databaseConnection.rawQuery("SELECT COUNT(*) FROM "+table_name+"",null);
            cursor.moveToFirst();
            return Integer.parseInt(cursor.getString(0));
        }
    }

    public static class DatabaseQueries{
        public void createTables(){
            databaseConnection.execSQL("CREATE TABLE IF NOT EXISTS USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)");
            databaseConnection.execSQL("CREATE TABLE IF NOT EXISTS WALLETS (id_wallet INTEGER PRIMARY KEY, id_user INTEGER NOT NULL REFERENCES USERS(id_user), bytecoin REAL NOT NULL)");
            databaseConnection.execSQL("CREATE TABLE IF NOT EXISTS LOGS (sender_wallet INTEGER NOT NULL, receiver_wallet NOT NULL, transaction_date TEXT NOT NULL)");
        }
    }

    public static class UserQueries{
        public void insertUser(String username, String password){
            if (DatabaseMethods.getTableLen("USERS") < 1 && DatabaseMethods.getTableLen("WALLETS") < 1) {
                databaseConnection.execSQL("INSERT INTO USERS (username, password) VALUES ('"+username+"', '"+CryptoMethods.getMD5(password)+"')");
                databaseConnection.execSQL("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES (10001, 1, 0)");
            }else{
                int lastId, lastWalletId;
                Cursor cursor = databaseConnection.rawQuery("SELECT id_user FROM WALLETS;", null);
                cursor.moveToLast();
                lastId = Integer.parseInt(cursor.getString(0));

                cursor = databaseConnection.rawQuery("SELECT id_wallet FROM WALLETS;", null);
                cursor.moveToLast();
                lastWalletId = Integer.parseInt(cursor.getString(0));

                lastId+=1;
                lastWalletId+=1;

                databaseConnection.execSQL("INSERT INTO USERS (username, password) VALUES ('"+username+"', '"+CryptoMethods.getMD5(password)+"')");
                databaseConnection.execSQL("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES ("+lastWalletId+", "+lastId+", 0)");
            }
        }
    }

    public static class WalletQueries{
    }

    public static class CryptoMethods{
        public static String getMD5(String input){
            try{
                MessageDigest md = MessageDigest.getInstance("MD5");
                byte[] messageDigest = md.digest(input.getBytes());
                BigInteger number = new BigInteger(1, messageDigest);
                String hashtext = number.toString(16);
                while (hashtext.length() < 32){ hashtext = "0" + hashtext; }
                return hashtext;
            }catch (NoSuchAlgorithmException e){throw new RuntimeException(e);}
        }
    }
}
