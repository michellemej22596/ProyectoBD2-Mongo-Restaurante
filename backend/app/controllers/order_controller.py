from app.models.order import OrdenCreate, OrdenResponse

@router.post("/", response_model=OrdenResponse)
async def create_orden(orden: OrdenCreate):
    orden_dict = orden.dict()
    result = await db["ordenes"].insert_one(orden_dict)
    return await db["ordenes"].find_one({"_id": result.inserted_id})