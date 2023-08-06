=======
History
=======

1.2.2 (2022-07-16)
------------------

* Bug fix: erroneous .to_list calls at utils.display_loan was raising AttributeError

1.2.1 (2021-10-01)
------------------

* Bug fix: annual interest rate not being properly converted to a daily
  interest rate

1.2.0 (2020-12-17)
------------------

* Implement Newton-Raphson based solver to approximate IRR
* Remove dependency on `scipy` and `numpy`
* Expand on grossup documentation
* Implement function `interest_rate.convert_to_daily_interest_rate`

1.1.0 (2020-10-15)
------------------

* Remove generic grossup solver. Only direct implementation of mathematical
  models should be encouraged

* drop python 2 support

1.0.0 (2020-02-03)
------------------

* Public API

0.1.0 (2019-11-10)
------------------

* First release on PyPI.
