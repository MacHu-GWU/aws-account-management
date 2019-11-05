Setup Business Unit Master Account
==============================================================================

Let's say you are

1. Create an AWS account for each Department
2. Follow the process in ``01-Setup-Organization-Master-Account``, setup root account and admin User.
3. Give the admin user the access


**Assume Role**:

For big Organiztion, **it is always a bad idea to maintain multiple IAM User in different AWS Account representing the same Person**. Because it makes it harder to track activity did by the same person, and also managing multiple sensitive credential may greatly increase the propability of leaking. In addition, assume-role makes it easy to switch between multiple AWS Account, instead of typing credentials.

Usually **we use Assume Role mechanism to grant an IAM User access to different account, or mocking a IAM User**.

To allow a IAM User to assume role, you have to allow ``sts:AssumeRole`` action.

IAM Policy ``arn:aws:iam::aws-account-id:policy/assume-any-role``

.. code-block:: python

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": [
                    "arn:aws:iam::<aws-account-id>:role/<role-name>"
                ]
            }
        ]
    }