import React, { useState, useEffect, forwardRef, useImperativeHandle } from "react";
import api from "../utils/api";
import "../styles/ProductAdmin.css";

const ProductAdmin = forwardRef((props, ref) => {
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [name, setName] = useState("");
    const [category_id, setCategory] = useState("");
    const [price, setPrice] = useState("");
    const [imageUrl, setPhotoUrl] = useState("")
    const [editMode, setEditMode] = useState(false);
    const [editProductId, setEditProductId] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {
        fetchProducts();
        fetchCategories();
    }, []);

    const fetchProducts = async () => {
        try {
            const response = await api.get("/furniture");
            setProducts(response.data);
        } catch (error) {
            console.error("Error fetching products:", error);
        }
    };

    const fetchCategories = async () => {
        try {
            const response = await api.get("categories/all");
            setCategories(response.data);
        } catch (error) {
            console.error("Error fetching categories:", error);
        }
    };

    useImperativeHandle(ref, () => ({
        fetchCategories,
    }));

    const addProduct = async (e) => {
        e.preventDefault();
        if (!name || !category_id || !price) {
            setError("Please fill in all required fields.");
            return;
        }

        const productData = {
            name,
            category: category_id, // Используйте "category", если сервер ожидает именно это.
            price,
            imageUrl,
        };        

        console.log("Product data to be sent:", productData);

        try {
            await api.post("/furniture/create", productData, {
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    "Content-Type": "application/json",
                },
            });
            fetchProducts();
            resetForm();
        } catch (error) {
            console.error("Error adding products:", error);
            setError("Failed to add product.");
        }
    };

    const resetForm = () => {
        setName("");
        setCategory(""); // Сбрасываем ID категории
        setPrice("");
        setPhotoUrl("");
        setError("");
        setEditMode(false);
        setEditProductId(null);
    };

    const startEditProduct = (product) => {
        setEditMode(true);
        setEditProductId(product._id);
        setName(product.name);
        setCategory(product.category?._id || "");
        setPrice(product.price);
        setPhotoUrl(product.imageUrl || "");
    };

    const editProduct = async (e) => {
        e.preventDefault();
        if (!name || !category_id || !price) {
            setError("Please fill in all required fields.");
            return;
        }

        const productData = {
            name,
            category_id,
            price,
            imageUrl,
        };

        try {
            await api.put(`/furniture/update/${editProductId}`, productData, {
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                    "Content-Type": "application/json",
                },
            });
            fetchProducts();
            resetForm();
        } catch (error) {
            console.error("Error updating product:", error);
            setError("Failed to update product");
        }
    };

    const deleteProduct = async (product) => {
        try {
            console.log("URL being called:", `/furniture/delete/${product._id}`);
            console.log("Authorization Header:", `Bearer ${localStorage.getItem("token")}`);

            await api.delete(`/furniture/delete/${product._id}`, {
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`,
            },
        });
            fetchProducts();
        } catch (error) {
            console.error("Error deleting product:", error);
        }
    };

    const handleCategorySelect = (selectedCategory) => {
        console.log("Selected category:", selectedCategory);
        setCategory(selectedCategory); // Устанавливаем категорию
    };

    return (
        <div className="product-admin">
            <h2>Manage Products</h2>
            {error && <div className="error">{error}</div>}
            <form
                onSubmit={editMode ? editProduct : addProduct}
                className="product-form"
            >
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="input-field"
                />
                <select
                    value={category_id}
                    onChange={(e) => handleCategorySelect(e.target.value)}
                    className="input-field"
                >
                    <option value="">Select Category</option>
                    {categories.map((m) => (
                        <option key={m._id} value={m._id}>
                            {m.name}
                        </option>
                    ))}
                </select>

                <input 
                    type="number"
                    placeholder="Price"
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                    className="input-field"
                />

                <input
                    type="text"
                    placeholder="Image URL"
                    value={imageUrl}
                    onChange={(e) => setPhotoUrl(e.target.value)}
                    className="input-field"
                />
                <button type="submit" className="submit-button">
                    {editMode ? "Update product" : "Add product"}
                </button>
                {editMode && (
                    <button type="button" onClick={resetForm} className="cancel-button">
                        Cancel
                    </button>
                )}
            </form>
            <div className="product-list">
                {products.map((product) => (
                    <div 
                        key={product._id}
                        className="product-item"
                    >
                        <div>
                            <h4>{product.name}</h4>
                            <p>Price: ${product.price}</p>
                            <p>Category: {product.category?.name || "Unknown"}</p>
                        </div>

                        <div>
                            <button onClick={() => startEditProduct(product)} className="edit-button">Edit</button>
                            <button onClick={() => deleteProduct(product)} className="delete-button">Delete</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
});

export default ProductAdmin;