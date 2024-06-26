"""This file contain the routers"""
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from sqlalchemy.orm import Session
from schemas import schema
from dependencies import subscription_service
from rabbitmq.producer import RabbitMQ
router = APIRouter(tags=['Sevice A'])

# rabbitmq class object
rabbitmq = RabbitMQ()

@router.get("/subscriptions", response_model=list[schema.Subscription], summary="Get all subscriptions")
async def get_all_subscriptions(db: Session = Depends(get_db)):
    """ Retrieve a list of all subscriptions."""
    return subscription_service.get_all_subscriptions(db)

@router.post('/subscriptions', response_model=schema.Subscription, summary="Create a new subscription")
async def create_subscription(request: schema.SubscriptionBase, db: Session = Depends(get_db)):
    """
    Create a new subscription.

    - **email**: The email address of the subscriber.
    - **is_active**: The status of the subscription (active - true or inactive - false).

    Returns:
        The details of the newly created subscription.
    """

    return subscription_service.create_subscription(db, email=request.email, is_active=request.is_active)

@router.put('/subscriptions/{subscription_id}', response_model=schema.Subscription, summary="Update a subscription")
async def update_subscription(subscription_id: int, request: schema.UpdateSubscription, db: Session = Depends(get_db)):
    """
    Update a subscription.

    - **subscription_id**: The ID of the subscription to be updated.
    - **is_active**: The updated status of the subscription (active or inactive).

    Returns:
        The details of the updated subscription.
    """
    subscription = subscription_service.get_subscription_by_id(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    try:
        subscription_instance = subscription_service.update_subscription(db, subscription, is_active=request.is_active)
        rabbitmq.publish_message(subscription_instance)
        return subscription_instance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # finally:
        # rabbitmq.close_connection()

@router.delete('/subscriptions/{subscription_id}', summary="Delete a subscription")
async def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    """
    Delete a subscription.

    - **subscription_id**: The ID of the subscription to be deleted.
    """
    subscription = subscription_service.get_subscription_by_id(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    subscription_service.delete_subscription(db, subscription)
    return {"message": "Subscription deleted successfully"}
