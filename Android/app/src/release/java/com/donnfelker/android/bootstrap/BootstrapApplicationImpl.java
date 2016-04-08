package com.opencv.andy.vision;

import com.crashlytics.android.Crashlytics;
import com.opencv.andy.vision.logging.CrashlyticsTree;

import io.fabric.sdk.android.Fabric;
import timber.log.Timber;

public class BootstrapApplicationImpl extends BootstrapApplication {
    @Override
    protected void onAfterInjection() {

    }

    @Override
    protected void init() {
        // Start Crashlytics.
        Fabric.with(this, new Crashlytics());

        // Set the type of logger, crashlytics in release mode
        Timber.plant(new CrashlyticsTree());
    }
}
