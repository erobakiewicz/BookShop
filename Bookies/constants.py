class OrderStatuses:
	EDITABLE = 10
	WAITING_FOR_PAYMENT = 20
	COMLETED = 30
	CANCELED = 40

	Choices = (
		(EDITABLE, 'Editable'),
		(WAITING_FOR_PAYMENT, 'Waiting for payment'),
		(COMLETED, 'Completed'),
		(CANCELED, 'Canceled'),
	)