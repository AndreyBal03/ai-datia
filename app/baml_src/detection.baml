
function GetTrayProducts(tray: image) -> string[]{
    client CustomGemini
    prompt #"
        {{_.role("system")}}
        You are an expert in identifying food products from images given by the user.
        Your main task is to identify which objects exist in the image.

        {{_.role("user")}}
        Analyze the image and list all the food products present in the tray.
        Provide the output as a JSON array of strings.
        
        Image Description: {{ tray }}
        
        {{ ctx.output_format }}
    "#
}


function GetProductExp(product: image) -> string{
    client CustomGemini
    prompt #"
        {{_.role("system")}}
        You are an expert in providing expiration date of food products from images given by the user.
        Your main task is to describe the food expiration in detail.
        in the following format:

        YYYY-MM-DDTHH:MM:SSZ

        {{_.role("user")}}
        Analyze the image and provide a detailed expiration date of the food product.
        
        Image :{{ product }}
        
        {{ ctx.output_format }}
    "#
}