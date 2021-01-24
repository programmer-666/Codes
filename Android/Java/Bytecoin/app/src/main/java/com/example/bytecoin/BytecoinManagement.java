package com.example.bytecoin;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;

/*
 *
 * BytecoinManagement Class Version 1.92
 * suhaarslan.com (c) 2020-2021
 *
 */

public class BytecoinManagement {

    protected static SQLiteDatabase databaseConnection; // SQLITE_DATABASE_CONNECTION

    public DatabaseQueries databaseQueries;
    public UserQueries userQueries;
    public CryptoMethods cryptoMethods;
    public WalletQueries walletQueries;
    public SessionManagement sessionManagement;
    public DatabaseMethods databaseMethods;

    public BytecoinManagement(SQLiteDatabase connection){
        databaseConnection = connection;

        this.databaseQueries = new DatabaseQueries();
        this.databaseMethods = new DatabaseMethods();
        this.userQueries = new UserQueries();
        this.cryptoMethods = new CryptoMethods();
        this.walletQueries = new WalletQueries();
        this.sessionManagement = new SessionManagement();
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
            databaseConnection.execSQL("CREATE TABLE IF NOT EXISTS LOGS (sender_wallet INTEGER NOT NULL, receiver_wallet NOT NULL, transaction_date TEXT NOT NULL, amount REAL NOT NULL)");
            UserQueries.BytecoinWallet();
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

        public static void BytecoinWallet(){
            databaseConnection.execSQL("INSERT INTO USERS (username, password) VALUES ('bycw', '"+CryptoMethods.getMD5("bycw123")+"');");
            databaseConnection.execSQL("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES (1001, 1, 100);");
        }

        public int getIdByUsername(String username){
            int uid = -1;

            Cursor cursor = databaseConnection.rawQuery("SELECT * FROM USERS;", null);
            for(int i = 0;i < DatabaseMethods.getTableLen("USERS");i++){
                cursor.moveToPosition(i);
                if(cursor.getString(1).equalsIgnoreCase(username)){
                    uid = Integer.parseInt(cursor.getString(0));
                    break;
                }else{
                    uid = -1;
                }
            }
            return uid;
        }

        public ArrayList<String> getInfoFromUserPassw(String username, String password){
            ArrayList<String> infos = new ArrayList<>();
            if (SessionManagement.loginControl(username, password) == true){
                int uid = getIdByUsername(username);
                Cursor cursor = databaseConnection.rawQuery("SELECT * FROM WALLETS WHERE id_user="+uid+"", null);
                cursor.moveToFirst();
                infos.add(cursor.getString(0));
                infos.add(String.valueOf(uid));
                infos.add(username);
                infos.add(password);
            }else{
                infos.add("notFind");
            }
            return infos;
        }
    }

    public static class WalletQueries{
        public double getAmountByWalletId(int walletId){
            Cursor cursor = databaseConnection.rawQuery("SELECT bytecoin FROM WALLETS WHERE id_wallet="+walletId+"", null);
            cursor.moveToFirst();
            return Double.parseDouble(cursor.getString(0));
        }

        public double getAmountByUserId(int uid){
            Cursor cursor = databaseConnection.rawQuery("SELECT bytecoin FROM WALLETS WHERE id_user="+uid+"", null);
            cursor.moveToFirst();
            return Double.parseDouble(cursor.getString(0));
        }

        public double getAmountByUsername(String username){
            Cursor cursor = databaseConnection.rawQuery("SELECT bytecoin FROM WALLETS JOIN USERS ON WALLETS.id_user=USERS.id_user;", null);
            cursor.moveToFirst();
            return Double.parseDouble(cursor.getString(0));
        }

        public boolean sendBytecoin(int srcWalletId, int dstWalletId, double amount){
            if (srcWalletId != dstWalletId){
                double srcwa = getAmountByWalletId(srcWalletId), dstwa = getAmountByWalletId(dstWalletId);
                if (srcwa-amount >= 0){
                    databaseConnection.execSQL("UPDATE WALLETS SET bytecoin="+(double)(srcwa-amount)+" WHERE id_wallet="+srcWalletId+"");
                    databaseConnection.execSQL("UPDATE WALLETS SET bytecoin="+(double)(dstwa+amount)+" WHERE id_wallet="+dstWalletId+"");
                    databaseConnection.execSQL("INSERT INTO LOGS VALUES ("+srcWalletId+", "+dstWalletId+", DATETIME('now'), '"+amount+"');");
                    return true;
                }else{
                    return false;
                }
            }else{
                return false;
            }
        }

        public ArrayList<ArrayList> getLogs(){
            ArrayList<String> srcWallets = new ArrayList<>();
            ArrayList<String> dstWallets = new ArrayList<>();
            ArrayList<String> transaction_dates = new ArrayList<>();
            ArrayList<String> amounts = new ArrayList<>();

            ArrayList<ArrayList> logs = new ArrayList<>();
            logs.add(srcWallets);logs.add(dstWallets);logs.add(transaction_dates);logs.add(amounts);

            Cursor cursor = databaseConnection.rawQuery("SELECT * FROM LOGS;", null);
            for (int i = 0;i<DatabaseMethods.getTableLen("LOGS");i++){
                cursor.moveToPosition(i);
                srcWallets.add(cursor.getString(0));
                dstWallets.add(cursor.getString(1));
                transaction_dates.add(cursor.getString(2));
                amounts.add(cursor.getString(3));
            }
            return logs;
        }
    }

    public static class SessionManagement{
        public static boolean loginControl(String username, String password){
            boolean status = false;
            Cursor cursor = databaseConnection.rawQuery("SELECT * FROM USERS;", null);
            for(int i = 0;i < DatabaseMethods.getTableLen("USERS");i++){
                cursor.moveToPosition(i);
                if (cursor.getString(1).equalsIgnoreCase(username) &&
                        cursor.getString(2).equalsIgnoreCase(CryptoMethods.getMD5(password))){
                    status = true;
                    break;
                }else{
                    status = false;
                }
            }
            return status;
        }
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
