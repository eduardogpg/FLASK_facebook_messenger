{
	"_id" : ObjectId("57e2a706b93c0d8d5ce74158"),
	"title" : "Mensaje de bienvenida",
	"content" : "Hola {first_name} me complace anunciarte que hemos registrados tus datos correctamente :D ",
	"context" : "welcome",
	"type" : "common",
	"order" : 1,
	"format" : true,
	"type_message" : "text_message"
}
{
	"_id" : ObjectId("57e2a706b93c0d8d5ce74159"),
	"title" : "Presentación",
	"content" : "Mi nombre es botFacilito, espero nos llevemos bien a lo largo del curso!",
	"context" : "welcome",
	"type" : "common",
	"order" : 2,
	"type_message" : "text_message"
}
{
	"_id" : ObjectId("57e2a706b93c0d8d5ce7415a"),
	"title" : "Obtener info",
	"content" : "Antes de comenzar necesito recabar cierta información, espero no te moleste",
	"context" : "welcome",
	"type" : "common",
	"order" : 3,
	"type_message" : "text_message"
}
{
	"_id" : ObjectId("57e2aad9b93c0d8d5ce7415b"),
	"title" : "obtener preferencias",
	"content" : "¿Cúal es tu color favorito?",
	"context" : "welcome",
	"type" : "not common",
	"order" : 4,
	"type_message" : "quick_replies",
	"replies" : [
		{
			"title" : "Red",
			"payload" : "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED"
		},
		{
			"title" : "Blue",
			"payload" : "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_BLUE"
		}
	]
}
{
	"_id" : ObjectId("57e2babeb93c0d8d5ce7415d"),
	"title" : "Ubicación",
	"content" : "¿Cual es tu locación?",
	"type" : "common",
	"context" : "welcome",
	"order" : 5,
	"type_message" : "quick_replies_location"
}
{
	"_id" : ObjectId("57e4000d3c939389b45df983"),
	"title" : "Clima info",
	"content" : "Actualmente {city} se encuentra a {temperature} grados centigrados",
	"context" : "temperature",
	"type" : "specific",
	"order" : 1,
	"format" : true,
	"type_message" : "text_message"
}