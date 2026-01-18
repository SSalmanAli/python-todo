"use client";

import React from 'react';
import Link from 'next/link';

const SignupPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Account Registration
          </h2>
        </div>
        <div className="text-center py-6">
          <p className="text-gray-600 mb-6">
            Currently, account registration is handled externally. Please contact your administrator to create an account.
          </p>

          <div className="mt-8">
            <p className="text-gray-600">
              Already have an account?
            </p>
            <Link href="/auth/login" className="mt-2 inline-block px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 text-sm font-medium">
              Sign in
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignupPage;