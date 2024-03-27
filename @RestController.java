@RestController
@RequestMapping("/api/products")
public class ProductController {

    private List<Product> products = new ArrayList<>(); // Replace with data access logic

    @GetMapping
    public List<Product> getAllProducts() {
        return products;
    }

    @PostMapping
    public Product createProduct(@RequestBody Product product) {
        products.add(product);
        return product;
    }
    // ... other endpoints for updating, deleting, etc.
}
