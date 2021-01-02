package com.example.bytecoindva1_512;

import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.LinearInterpolator;
import android.view.animation.RotateAnimation;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class bycmain extends AppCompatActivity {
    SQLiteDatabase sqLiteDatabase;
    BytecoinManagement bytecoinManagement;
    TextView walletid,byctext;
    ImageView refresh;
    ArrayList<String> userInfos;

    EditText amount, dstwid;
    Button send;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bycmain);

        amount = findViewById(R.id.sendBycA);
        dstwid = findViewById(R.id.dstwid);
        send = findViewById(R.id.buttonSend);

        walletid = findViewById(R.id.walletIdText);
        byctext = findViewById(R.id.bycText);
        refresh = findViewById(R.id.refreshImage);

        refreshInfo();

        // FIRST

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sqLiteDatabase = openOrCreateDatabase("bytecoin_dva1_512.db", MODE_PRIVATE, null);
                bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

                ArrayList<String> infos = bytecoinManagement.userQueries.getInfoFromUserPassw(getIntent().getExtras().getString("username"), getIntent().getExtras().getString("password"));
                    if (bytecoinManagement.walletQueries.sendBytecoin(Integer.parseInt(infos.get(0)), Integer.parseInt(dstwid.getText().toString()), Double.parseDouble(amount.getText().toString()))){
                        Toast.makeText(bycmain.this, "Success", Toast.LENGTH_SHORT).show();
                    }else{
                        Toast.makeText(bycmain.this, "Failed", Toast.LENGTH_SHORT).show();
                    }

                bytecoinManagement.closeDatabaseConnection();
            }
        });
    }

    public void refreshInfo(){
        sqLiteDatabase = openOrCreateDatabase("bytecoin_dva1_512.db", MODE_PRIVATE, null);
        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);
        userInfos = bytecoinManagement.userQueries.getInfoFromUserPassw(getIntent().getExtras().getString("username"), getIntent().getExtras().getString("password"));

        walletid.setText(userInfos.get(0));
        byctext.setText(String.valueOf(bytecoinManagement.walletQueries.getAmountByWalletId(Integer.parseInt(userInfos.get(0)))));

        bytecoinManagement.closeDatabaseConnection();
    }

    public void rotateRefresh(){
        RotateAnimation rotate = new RotateAnimation(0, 180, Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        rotate.setDuration(500);
        rotate.setInterpolator(new LinearInterpolator());
        refresh.startAnimation(rotate);
    }

    public void refreshStatus(View v){
        rotateRefresh();
        sqLiteDatabase = openOrCreateDatabase("bytecoin_dva1_512.db", MODE_PRIVATE, null);
        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);
        userInfos = bytecoinManagement.userQueries.getInfoFromUserPassw(getIntent().getExtras().getString("username"), getIntent().getExtras().getString("password"));
        walletid.setText(userInfos.get(0));
        byctext.setText(String.valueOf(bytecoinManagement.walletQueries.getAmountByWalletId(Integer.parseInt(userInfos.get(0)))));
        bytecoinManagement.closeDatabaseConnection();
    }
}