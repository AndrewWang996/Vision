package com.opencv.andy.vision;

import android.accounts.AccountsException;
import android.app.Activity;

import com.opencv.andy.vision.core.BootstrapService;

import java.io.IOException;

public interface BootstrapServiceProvider {
    BootstrapService getService(Activity activity) throws IOException, AccountsException;
}
