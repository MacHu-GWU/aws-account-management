Setup Organization Master Account
==============================================================================

.. contents::
    :local:


Step1. Delete root User's Access Key
------------------------------------------------------------------------------

Disable program access for root account


Step2. Activate MFA on your root account
------------------------------------------------------------------------------

Properly store the ROOT account email / password and your MFA device, and give this credential to Very Trustworthy people, like your CTO. Whoever has this credential can do anything to anything to any of your AWS Account, which is GOD!


Step3. Create an ``Admin`` User Group
------------------------------------------------------------------------------

Create an IAM Group called ``Admin`` and attach the ``arn:aws:iam::aws:policy/AdministratorAccess`` Policy. Any IAM User added to this Group will have the full access to the master Account.

So far, you don't have any IAM User created yet.


Step4. Create an IAM User for AWS Administrator Head
------------------------------------------------------------------------------

Let's say you hired a Senior AWS Administrator Alice. Create an IAM User representing the specific person, Alice. The user name should be very unique, I recommend to use ``<firstname>.<lastname>`` naming convention for the username. Grant IAM User ``Alice`` programatic access and console access. Add ``Alice`` to ``Admin`` Group.


Step5. Setup IAM Group for Landing Zone
------------------------------------------------------------------------------

Everytime you got a new hire that requires AWS Account access, create an IAM User using the above naming convention for him. And add the User to Landing Zone IAM User Group.

Landing Zone is an IAM User Group represent a stage that requires new IAM User to finish setup password or MFA (Based on your Organization Authentication Policy). Once he finished the on-boarding, you can grant this User corresponding access.

**Create an IAM Policy called** ``arn:aws:iam::aws-account-id:policy/landing-zone``

.. code-block:: python

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowUserToUpdateTheirOwnPassword",
                "Effect": "Allow",
                "Action": [
                    "iam:UpdateLoginProfile",
                    "iam:ChangePassword"
                ],
                "Resource": [
                    "arn:aws:iam::aws-account-id:user/${aws:username}"
                ]
            },
            {
                "Sid": "AllowUserToUpdateTheirVirtualMFADevice",
                "Effect": "Allow",
                "Action": "iam:*VirtualMFADevice",
                "Resource": "arn:aws:iam::aws-account-id:mfa/${aws:username}"
            },
            {
                "Sid": "AllowUserToUpdateMFADeviceConfig",
                "Effect": "Allow",
                "Action": [
                    "iam:DeactivateMFADevice",
                    "iam:EnableMFADevice",
                    "iam:ResyncMFADevice"
                ],
                "Resource": "arn:aws:iam::aws-account-id:user/${aws:username}"
            }
        ]
    }

**Create an IAM Group called** landing-zone, attach two IAM Policies, ``arn:aws:iam::aws-account-id:policy/landing-zone`` and ``arn:aws:iam::aws:policy/IAMReadOnlyAccess``.

By doing this, any IAM User in landing-zone Group can modify their own password and setup MFA.


Step6. Deny create IAM User policy
------------------------------------------------------------------------------



**Deny create IAM User**:

Usually you should not allow a regular IAM User to create other IAM Users. And only allow the ``Admin`` to do that. Because if User A creates another User B, then use User B to perform some malicious action and delete the User B afterward, it is harder to track originally who did the action.
