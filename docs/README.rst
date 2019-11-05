Setup IAM for Hybird Account Structure
==============================================================================

This tutorial help you walk through the setup process for Hybird Account Structure. Firstly you have multiple departments, and each department has its own department account. And each department has multiple products, each product has multi aws account to isolate different stage.

Let's use Facebook as example.

.. code-block:: python

    Master Account
    |--- IT Department
        |--- Facebook.com website Project dev
        |--- Facebook.com website Project test
        |--- Facebook.com website Project prod
        |--- Facebook.com messenger Project dev
        |--- Facebook.com messenger Project test
        |--- Facebook.com messenger Project prod
        |--- Instagram Project dev
        |--- Instagram Project test
        |--- Instagram Project prod
        |--- ...
    |--- HR Department
        |--- ...
    |--- Finance Department
        |--- ...
    |--- Marketing Department
        |--- ...
