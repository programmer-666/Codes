package com.example.bytecoin;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.database.sqlite.SQLiteDatabase;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.LinearInterpolator;
import android.view.animation.RotateAnimation;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class bytecoinMain extends AppCompatActivity {

    TextView walletID, bycAmount;
    ImageView refreshImage;

    Button sendButton;
    EditText dstWalletID, amount;

    SQLiteDatabase sqLiteDatabase;
    BytecoinManagement bytecoinManagement;

    ArrayList<String> userInfos;

    ScrollView scrollView;
    LinearLayout scLinearLayout;
    ArrayList<TextView> textViews;

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bytecoin_main);

        walletID = findViewById(R.id.walletIDText);
        bycAmount = findViewById(R.id.bycAmountText);

        dstWalletID = findViewById(R.id.dstWalletID);
        amount = findViewById(R.id.amount);
        sendButton = findViewById(R.id.sendButton);

        scrollView = findViewById(R.id.scrollView);
        scLinearLayout = findViewById(R.id.scrollViewLinearLayout);
        ArrayList<TextView> textViews;

        refreshImage = findViewById(R.id.refreshImage);

        refresStatus();

        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sqLiteDatabase = openOrCreateDatabase("bytecoin.db", MODE_PRIVATE, null);
                bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

                ArrayList<String> infos = bytecoinManagement.userQueries.getInfoFromUserPassw(getIntent().getExtras().getString("username"), getIntent().getExtras().getString("password"));
                if (bytecoinManagement.walletQueries.sendBytecoin(Integer.parseInt(infos.get(0)), Integer.parseInt(dstWalletID.getText().toString()), Double.parseDouble(amount.getText().toString()))){
                    Toast.makeText(getBaseContext(), "Successful", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(getBaseContext(), "Failed", Toast.LENGTH_SHORT).show();
                }
                bytecoinManagement.closeDatabaseConnection();

                //refresStatus();
            }
        });
    }

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)
    public void refresStatus(){
        sqLiteDatabase = openOrCreateDatabase("bytecoin.db", MODE_PRIVATE, null);
        bytecoinManagement = new BytecoinManagement(sqLiteDatabase);

        userInfos = bytecoinManagement.userQueries.getInfoFromUserPassw(getIntent().getExtras().getString("username"), getIntent().getExtras().getString("password"));
        bycAmount.setText(String.valueOf(bytecoinManagement.walletQueries.getAmountByWalletId(Integer.parseInt(userInfos.get(0)))));
        walletID.setText(userInfos.get(0));

        textViews = new ArrayList<>();
        scLinearLayout.removeAllViews();
        for(int i = 0;i < bytecoinManagement.databaseMethods.getTableLen("LOGS");i++){
            textViews.add(new TextView(this));
            textViews.get(i).setText((String)bytecoinManagement.walletQueries.getLogs().get(0).get(i)+" > "+(String)bytecoinManagement.walletQueries.getLogs().get(1).get(i)+" [ "+(String)bytecoinManagement.walletQueries.getLogs().get(2).get(i)+" ] "+bytecoinManagement.walletQueries.getLogs().get(3).get(i)+" BYC");
            textViews.get(i).setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
            scLinearLayout.addView(textViews.get(i));
        }

        bytecoinManagement.closeDatabaseConnection();
    }

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN_MR1)
    public void refreshImage(View v){
        RotateAnimation rotate = new RotateAnimation(0, 180, Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        rotate.setDuration(500);
        rotate.setInterpolator(new LinearInterpolator());
        refreshImage.startAnimation(rotate);
        refresStatus();
    }
}