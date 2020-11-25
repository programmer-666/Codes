package com.example.frapp;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

public class PagerViewAdapter extends FragmentPagerAdapter {

    public PagerViewAdapter(@NonNull FragmentManager fm) {
        super(fm);
    }

    @NonNull
    @Override
    public Fragment getItem(int position) {
        Fragment frt = null;
        switch (position){
            case 0:
                frt = new wallet_fragment();
                break;
            case 1:
                frt = new profile_fragment();
                break;
            case 2:
                frt = new send_fragment();
                break;
        }
        return frt;
    }

    @Override
    public int getCount() {
        return 3;
    }
}
